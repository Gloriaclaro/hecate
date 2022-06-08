from networkx import Graph

from hecate.domain.entities.edge import EdgeSignal
from hecate.domain.entities.middle_signal import MiddleSignal
from hecate.domain.entities.n_signal import NSignal
from hecate.domain.entities.p_signal import PSignal
from hecate.services.read_circuit import ReadCircuit


class CreateCircuit:

    def __init__(self, graph: Graph, circuit_reader: ReadCircuit):
        self.circuit = graph
        self.circuit_reader = circuit_reader

    def create_nodes(self):
        nodes = self.circuit_reader.get_signals_list()
        self.circuit.add_nodes_from(nodes)

    def create_edges_pull_up(self):
        for transistor in self.circuit_reader.p_transistors_list:
            self.circuit.add_edges_from([
                (transistor.get_drain_name(), f"p_{transistor.get_gate_name()}", {"signal": EdgeSignal()}),
                (f"p_{transistor.get_gate_name()}", transistor.get_source_name(), {"signal": EdgeSignal()}),
            ])

    def create_edges_pull_down(self):
        for transistor in self.circuit_reader.n_transistors_list:
            self.circuit.add_edges_from([
                (transistor.get_drain_name(), f"n_{transistor.get_gate_name()}", {"signal": EdgeSignal()}),
                (f"n_{transistor.get_gate_name()}", transistor.get_source_name(), {"signal": EdgeSignal()}),
            ])

    def create_edges_between_two_middle_nodes(self):
        ...

    def create_edges_in_node_out_in(self):
        ...

    def show_edges(self):
        for n, nbrs in self.circuit.adj.items():
            print(n, nbrs)

    def show_nodes(self):
        print(self.circuit.nodes.data())