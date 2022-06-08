from networkx import Graph


class IdentifySensitiveNodes:

    def __init__(self, output, possible_sensitive: list, circuit: Graph):
        self.sensitive_nodes = [output]
        self.possible_sensitive_nodes = possible_sensitive
        self.circuit = circuit

    def find_sensitive_nodes(self):
        for node in self.possible_sensitive_nodes:
            node_signal_value = self.circuit.nodes[node]["signal"].get_signal_value()
            node_signal = self.circuit.nodes[node]["signal"]
            if node_signal_value == 0 and node_signal.get_signal_bulk() == 1:
                self.sensitive_nodes.append(node)
            elif node_signal_value == 1 and node_signal.get_signal_bulk() == 0:
                self.sensitive_nodes.append(node)
