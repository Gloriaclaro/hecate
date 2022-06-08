from networkx import Graph
from hecate.domain.entities.circuit_metadata import CircuitMetadata
from hecate.domain.entities.middle_signal import MiddleSignal
from hecate.domain.entities.n_signal import NSignal
from hecate.domain.entities.p_signal import PSignal


class GenerateSignalPath:

    def __init__(self, circuit: Graph, circuit_reader: CircuitMetadata):
        self.circuit = circuit
        self.last_signal = None
        self.circuit_metadata = circuit_reader
        self.next_nodes = []
        self.visited_nodes = []
        self.output = circuit_reader.get_output()
        self.last_node = None

    def generate_signal_path_pull_up(self):
        last_node = self.circuit_metadata.get_supply()
        last_signal = 1
        self.visited_nodes = [last_node]
        self.recursive_find_next_nodes(last_node, last_signal)

    def generate_signal_path_pull_down(self):
        last_node = self.circuit_metadata.get_ground()
        last_signal = 0
        self.visited_nodes = [last_node]
        self.recursive_find_next_nodes(last_node, last_signal)

    def recursive_find_next_nodes(self, last_node, last_signal):
        self.next_nodes = self.get_next_node(last_node)
        for node in self.next_nodes:
            if node in self.visited_nodes:
                continue
            last_signal = self.set_signals(last_signal, last_node, node)
            if node == self.output:
                continue
            self.visited_nodes.append(node)

            self.recursive_find_next_nodes(node, last_signal)

    def generate_signals_path_from_out(self):
        last_node = self.circuit_metadata.get_output()
        last_signal = self.circuit.nodes[last_node]["signal"].get_signal_value()
        if last_signal == 0:
            self.recursive_find_predecessor_nodes_pull_up(last_node, last_signal)
        elif last_signal == 1:
            self.recursive_find_predecessor_nodes_pull_down(last_node, last_signal)

    def recursive_find_predecessor_nodes_pull_up(self, last_node: str, last_signal: int):
        self.next_nodes = self.get_next_node(last_node)
        for node in self.next_nodes:
            node_signal = self.circuit.nodes[node]["signal"]
            if node in self.visited_nodes:
                continue
            if isinstance(node_signal, NSignal):
                break
            last_signal = self.set_signal_from_out(last_signal, last_node, node)
            if isinstance(node_signal, PSignal) and node_signal.get_signal_value() == 1:
                continue
            self.visited_nodes.append(node)
            self.recursive_find_predecessor_nodes_pull_up(node, last_signal)

    def recursive_find_predecessor_nodes_pull_down(self, last_node: str, last_signal: int):
        self.next_nodes = self.get_next_node(last_node)
        for node in self.next_nodes:
            node_signal = self.circuit.nodes[node]["signal"]
            if node in self.visited_nodes:
                continue

            if isinstance(node_signal, PSignal):
                continue

            last_signal = self.set_signal_from_out(last_signal, last_node, node)
            if isinstance(node_signal, NSignal) and node_signal.get_signal_value() == 0:
                continue
            self.recursive_find_predecessor_nodes_pull_down(node, last_signal)
            self.visited_nodes.append(node)

    def set_signals(self, last_signal, node, next_node):
        node_signal = self.circuit.nodes[node]["signal"]
        last_signal = node_signal.set_edge_signal(last_signal, node, next_node, self.circuit)
        return last_signal

    def set_signal_from_out(self, last_signal, node, next_node):
        next_node_signal = self.circuit.nodes[next_node]['signal']
        if self.circuit[next_node][node]["signal"].get_signal_value() == 'x':
            self.circuit[next_node][node]['signal'].set_signal_value(last_signal)
            self.circuit[next_node][node]['value'] = last_signal
        if isinstance(next_node_signal, MiddleSignal) and self.circuit.nodes[next_node]['signal'].get_signal_value() == 'x':
            self.circuit.nodes[next_node]['signal'].set_signal_value(last_signal)
        return last_signal

    def get_next_node(self, node_name: str):
        adj_node = self.circuit.adj[node_name]
        return list(adj_node._atlas)

    def set_inputs_high(self):
        for input_name in self.circuit_metadata.get_inputs():
            self.circuit.nodes[f"p_{input_name}"]["signal"].set_signal_value(1)
            self.circuit.nodes[f"n_{input_name}"]["signal"].set_signal_value(1)

    def set_input_values(self):
        for input_name in self.circuit_metadata.get_inputs():
            value = int(input(f"Set value for {input_name}: \n"))
            self.circuit.nodes[f"p_{input_name}"]["signal"].set_signal_value(value)
            self.circuit.nodes[f"n_{input_name}"]["signal"].set_signal_value(value)