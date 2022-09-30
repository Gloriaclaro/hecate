from hecate.generate_inputs import GenerateInputs
from hecate.identify_sensitive_nodes import IdentifySensitiveNodes
from hecate.netlist import Netlist
from hecate.propagate_signal import FindSignalsValue
from pathlib import Path
from os.path import join as path_concat

from hecate.signal import Signal


class Hecate:
    BASE_PATH = Path(__file__).parent

    def __init__(self, circuit_name: str):
        self.netlist = Netlist(circuit_name)
        self.circuit = circuit_name
        self.signal_path = FindSignalsValue(self.netlist)
        self.identify = IdentifySensitiveNodes(self.netlist)

    def vector_by_sensitive_node(self, node: str):
        self.netlist.read_ngspice_file()
        node_signal = self.netlist.signals.get(node)
        inputs = GenerateInputs(
            inputs=self.netlist.input_signals_list
        )
        vectors = inputs.get_all_input_vectors()
        with open(path_concat(self.BASE_PATH, "outputs", "analysis_by_node", self.circuit + ".txt"), 'w') as output:
            output.write(f'Node {node_signal.name} \n')

            for vector in vectors:
                self.signal_path.generate_input_values(**vector)
                self.signal_path.generate_output_values()
                is_sensitive = self.identify.find_sensitive_node(node_signal)
                if is_sensitive:
                    output.write(''.join(str(val) for val in vector.values())+ "\n")
                self.identify.reset_sensitive_nodes()
                self.signal_path.reset()

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
                output.write(
                    ''.join(str(val) for val in vector.values())
                    + " | " + str(self.identify.sensitive_nodes) + "\n"
                )
                self.identify.reset_sensitive_nodes()
                self.signal_path.reset()


hecate = Hecate('circuit_paulo2')
# hecate.sensitive_nodes_for_all_input_values()
hecate.vector_by_sensitive_node("x1")

#TODO Nodo crítico, vetor crítico, analise por nodo trazendo os vatores