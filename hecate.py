from hecate.generate_inputs import GenerateInputs
from hecate.identify_sensitive_nodes import IdentifySensitiveNodes
from hecate.netlist import Netlist
from hecate.propagate_signal import FindSignalsValue
from pathlib import Path
from os.path import join as path_concat


class Hecate:
    BASE_PATH = Path(__file__).parent

    def __init__(self, circuit_name: str):
        self.netlist = Netlist(circuit_name)
        self.circuit = circuit_name
        self.signal_path = FindSignalsValue(self.netlist)
        self.identify = IdentifySensitiveNodes(self.netlist)
        self.sensitive_nodes = []

    def vector_by_sensitive_node(self, node: str):
        with open(path_concat(self.BASE_PATH, "outputs", "analysis_by_node", self.circuit + ".txt"), 'w') as output:
            output.write(f'Node {node} \n')
            for vector in self.sensitive_nodes:
                if node in vector.get('sensitive_nodes'):
                    output.write(vector.get('vector') + '\n')

    def critical_nodes(self):
        with open(path_concat(self.BASE_PATH, "outputs", "critical_nodes", self.circuit + ".txt"), 'w') as output:
            output.write(f'Node | #Vectors \n')

            sensitive_nodes = []
            for vector in self.sensitive_nodes:
                sensitive_nodes += vector.get('sensitive_nodes')
            nodes_set = set(sensitive_nodes)
            node_count = []
            for node in nodes_set:
                node_count.append((node, sensitive_nodes.count(node)))
            for node in sorted(node_count, key=lambda tup: tup[1], reverse=True):
                output.write(f'{node[0]} | {node[1]} \n')

    def critical_vectors(self):
        with open(path_concat(self.BASE_PATH, "outputs", "critical_vectors", self.circuit + ".txt"), 'w') as output:
            output.write(f'Vector | #Nodes count \n')
            sensitive_nodes = []
            for vector in self.sensitive_nodes:
                sensitive_nodes.append((vector.get('vector'), len(vector.get('sensitive_nodes'))))
            for node in sorted(sensitive_nodes, key=lambda tup: tup[1], reverse=True):
                output.write(f'{node[0]} | {node[1]} \n')

    def sensitive_nodes_for_all_input_values(self):
        self.netlist.read_ngspice_file()
        inputs = GenerateInputs(
            inputs=self.netlist.input_signals_list
        )
        vectors = inputs.get_all_input_vectors()
        with open(path_concat(self.BASE_PATH, "outputs", self.circuit + ".txt"), 'w') as output:
            output.write('vector | sensitive_node \n')
            for vector in vectors:
                self.signal_path.generate_input_values(**vector)
                self.signal_path.generate_output_values()
                self.identify.find_all_sensitive_nodes()
                str_vector = ''.join(str(val) for val in vector.values())
                output.write(
                    str_vector
                    + " | " + str(self.identify.sensitive_nodes) + "\n"
                )
                self.sensitive_nodes.append({"vector": str_vector, "sensitive_nodes": self.identify.sensitive_nodes})
                self.identify.reset_sensitive_nodes()
                self.signal_path.reset()


hecate = Hecate('c432')
hecate.sensitive_nodes_for_all_input_values()
hecate.vector_by_sensitive_node("N10")
hecate.critical_nodes()
hecate.critical_vectors()

#TODO Nodo crítico, vetor crítico, analise por nodo trazendo os vatores
#TODO tempo
#TODO cli
#TODO ABC parser
# Analise por vetor -> traz todos os nodos sensíveis para o vetor específico
# Analise por nodo -> traz a quantidade de vetores no qual os nodos são sensíveis