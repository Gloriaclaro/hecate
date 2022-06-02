from networkx import DiGraph

from hecate.services.create_circuit import CreateCircuit
from hecate.services.generate_signal_path import GenerateSignalPath
from hecate.services.read_circuit import ReadCircuit
from pathlib import Path
from os.path import join as path_concat

BASE_PATH = Path(__file__).parent

circuit_reader = ReadCircuit(path_concat(BASE_PATH, "circuit"))
circuit_reader.read_ngspice_file()
graph = DiGraph()

circuit = CreateCircuit(graph, circuit_reader)
circuit.create_nodes()
circuit.create_edges_pull_up()
circuit.create_edges_pull_down()
# circuit.create_edges_between_two_middle_nodes()
# circuit.show_edges()
#
signal_path = GenerateSignalPath(circuit.circuit, circuit_reader.circuit_metadata)
signal_path.set_inputs_high()
#
# circuit.show_nodes()
#
signal_path.generate_signal_path_pull_up()
signal_path.generate_signal_path_pull_down()
signal_path.generate_signals_path_from_out()

circuit.show_edges()
