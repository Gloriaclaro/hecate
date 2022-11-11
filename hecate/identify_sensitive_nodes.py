from typing import List

from hecate.netlist import Netlist
from hecate.signal import Signal


class IdentifySensitiveNodes:

    def __init__(self, circuit: Netlist):
        self.sensitive_nodes = []
        self.outputs = circuit.output_signals_list
        self.possible_sensitive_nodes = circuit.intern_signals_list
        self.inputs = circuit.input_signals_list

    def find_sensitive_node(self, node):
        node_value = node.get_signal_value()
        is_sensitive = False
        if node_value is None:
            return is_sensitive

        transistors = node.transistor_adj.values()

        for transistor in transistors:
            bulk = transistor.get_bulk().get_signal_value()

            if bulk != node_value:
                is_sensitive = True
        return is_sensitive

    def find_all_sensitive_nodes(self):
        for node in [*self.possible_sensitive_nodes, *self.outputs, *self.inputs]:
            # print(node.name,  node.get_signal_value())
            node_value = node.get_signal_value()
            if node_value is None:
                continue

            transistors = node.transistor_adj.values()

            for transistor in transistors:
                bulk = transistor.get_bulk().get_signal_value()

                if bulk != node_value and node not in self.sensitive_nodes:
                    self.sensitive_nodes.append(node)

    def reset_sensitive_nodes(self):
        self.sensitive_nodes = []

    def find_sensitive_nodes_from(self, possible_sensitive_list: List[Signal]):
        for node in [*possible_sensitive_list, *self.outputs]:
            node_value = node.get_signal_value()
            if node_value is None:
                continue

            transistors = node.transistor_adj.values()

            for transistor in transistors:
                bulk = transistor.get_bulk().get_signal_value()

                if bulk != node_value and node.name not in self.sensitive_nodes:
                    self.sensitive_nodes.append(node.name)