from networkx import Graph

from hecate.services.create_circuit import CreateCircuit
from hecate.services.generate_signal_path import GenerateSignalPath
from hecate.services.identify_sensitive_nodes import IdentifySensitiveNodes
from hecate.services.read_circuit import ReadCircuit
from pathlib import Path
from os.path import join as path_concat

BASE_PATH = Path(__file__).parent

circuit_reader = ReadCircuit(path_concat(BASE_PATH, "circuit"))
circuit_reader.read_ngspice_file()
graph = Graph()

circuit = CreateCircuit(graph, circuit_reader)
circuit.create_nodes()
circuit.create_edges_pull_up()
circuit.create_edges_pull_down()
# circuit.create_edges_between_two_middle_nodes()
# circuit.show_edges()
#
signal_path = GenerateSignalPath(circuit.circuit, circuit_reader.circuit_metadata)
signal_path.set_input_values()
#
#
signal_path.generate_signal_path_pull_up()
signal_path.generate_signal_path_pull_down()
signal_path.generate_signals_path_from_out()

# circuit.show_nodes()
circuit.show_edges()

possible_sensitive = circuit_reader.get_possible_sensitive_list()
output = circuit_reader.circuit_metadata.get_output()
sensitive_nodes = IdentifySensitiveNodes(output, possible_sensitive, signal_path.circuit)
sensitive_nodes.find_sensitive_nodes()
print(sensitive_nodes.sensitive_nodes)