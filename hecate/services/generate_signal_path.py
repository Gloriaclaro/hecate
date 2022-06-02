from typing import Union

from networkx import DiGraph

from hecate.domain.entities.circuit_metadata import CircuitMetadata
from hecate.domain.entities.middle_signal import MiddleSignal
from hecate.domain.entities.n_signal import NSignal
from hecate.domain.entities.p_signal import PSignal
from hecate.domain.entities.root_signal import RootSignal


class GenerateSignalPath:

    def __init__(self, circuit: DiGraph, circuit_reader: CircuitMetadata):
        self.circuit = circuit
        self.last_signal = None
        self.circuit_metadata = circuit_reader
        self.next_nodes = []

    def generate_signal_path_pull_up(self):
        self.next_nodes = [self.circuit_metadata.get_supply()]
        self.last_signal = 1
        last_node_signal_by_node = {}
        self.recursive_find_next_nodes(last_node_signal_by_node)

    def generate_signal_path_pull_down(self):
        self.next_nodes = [self.circuit_metadata.get_ground()]
        self.last_signal = 0
        last_node_signal_by_node = {}
        self.recursive_find_next_nodes(last_node_signal_by_node)

    def recursive_find_next_nodes(self, last_signal_by_node: dict):
        for node in self.next_nodes:
            self.next_nodes = self.get_next_node(node)
            if node not in list(last_signal_by_node.keys()):
                last_signal_by_node[node] = self.last_signal
            for next_node in self.next_nodes:
                self.last_signal = self.set_signals(last_signal_by_node[node], node, next_node)
                last_signal_by_node[next_node] = self.last_signal
            self.recursive_find_next_nodes(last_signal_by_node)

    def generate_signals_path_from_out(self):
        output_name = self.circuit_metadata.get_output()
        self.next_nodes = [self.circuit_metadata.get_output()]
        self.last_signal = self.circuit.nodes[output_name]["signal"].get_signal_value()
        last_node_signal_by_node = {}
        self.recursive_find_predecessor_nodes(last_node_signal_by_node)

    def recursive_find_predecessor_nodes(self, last_signal_by_node: dict):
        for node in self.next_nodes:
            self.next_nodes = self.get_predecessors(node)
            if node not in list(last_signal_by_node.keys()):
                last_signal_by_node[node] = self.last_signal
            for next_node in self.next_nodes:
                if isinstance(node, NSignal) and self.circuit.nodes[node]["signal"].get_signal_value() == 0:
                    break
                elif isinstance(node, PSignal) and self.circuit.nodes[node]["signal"].get_signal_value() == 1:
                    break
                else:
                    self.last_signal = self.set_signal_from_out(last_signal_by_node[node], node, next_node)
                    last_signal_by_node[next_node] = self.last_signal
            self.recursive_find_predecessor_nodes(last_signal_by_node)

    def set_signals(self, last_signal, node, next_node):
        node_signal = self.circuit.nodes[node]["signal"]
        last_signal = node_signal.set_edge_signal(last_signal, node, next_node, self.circuit)
        return last_signal

    def set_signal_from_out(self, last_signal, node, next_node):
        if self.circuit[next_node][node]["signal"].get_signal_value() == 'x':
            self.circuit[next_node][node]['signal'].set_signal_value(last_signal)
            self.circuit[next_node][node]['value'] = last_signal
        if isinstance(next_node, RootSignal) and self.circuit.nodes[next_node]['signal'].get_signal_value() == 'x':
            self.circuit.nodes[next_node]['signal'].set_signal_value(last_signal)
        return last_signal

    def get_next_node(self, node_name: str):
        adj_node = self.circuit.adj[node_name]
        return list(adj_node._atlas)

    def get_predecessors(self, key: str):
        pre_nodes = self.circuit.predecessors(key)
        return list(pre_nodes)

    def set_inputs_high(self):
        for input_name in self.circuit_metadata.get_inputs():
            self.circuit.nodes[f"p_{input_name}"]["signal"].set_signal_value(1)
            self.circuit.nodes[f"n_{input_name}"]["signal"].set_signal_value(1)