from typing import List

from hecate_v2.signal import Signal


class IdentifySensitiveNodes:

    def __init__(self, outputs: list, possible_sensitive: List[Signal]):
        self.sensitive_nodes = []
        self.outputs = outputs
        # self.sensitive_nodes = self.set_outputs_as_sensitive(outputs)
        self.possible_sensitive_nodes = possible_sensitive

    def find_sensitive_nodes(self):
        for node in [*self.possible_sensitive_nodes, *self.outputs]:
            node_value = node.get_signal_value()
            # print(node_value, node.name)
            if node_value is None:
                continue

            transistors = node.transistor_adj.values()

            for transistor in transistors:
                bulk = transistor.get_bulk().get_signal_value()

                if bulk != node_value and node.name not in self.sensitive_nodes:
                    self.sensitive_nodes.append(node.name)

    @staticmethod
    def set_outputs_as_sensitive(outputs: List[Signal]):
        return [output.name for output in outputs]
