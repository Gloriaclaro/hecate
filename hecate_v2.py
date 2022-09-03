from hecate_v2.generate_signal_path import GenerateSignalPath
from hecate_v2.identify_sensitive_nodes import IdentifySensitiveNodes
from hecate_v2.netlist import Netlist

netlist = Netlist("circuit_paulo2")
netlist.read_ngspice_file()

all_inputs = [
    {"a": 0, "b": 0, "c": 0},
    {"a": 0, "b": 0, "c": 1},
    {"a": 0, "b": 1, "c": 0},
    {"a": 0, "b": 1, "c": 1},
    {"a": 1, "b": 0, "c": 0},
    {"a": 1, "b": 0, "c": 1},
    {"a": 1, "b": 1, "c": 0},
    {"a": 1, "b": 1, "c": 1},
]
for input in all_inputs:
    netlist = Netlist("circuit_paulo3")
    netlist.read_ngspice_file()
    signal_path = GenerateSignalPath(netlist)
    signal_path.generate_input_values(a=input.get("a"), b=input.get("b"), c=input.get("c"))
    signal_path.find_path_from_outputs()

    identify = IdentifySensitiveNodes(netlist.output_signals_list, netlist.intern_signals_list)
    identify.find_sensitive_nodes()
    print(input.get("a"), input.get("b"), identify.sensitive_nodes)