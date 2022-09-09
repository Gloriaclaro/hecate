from hecate_v2.generate_signal_path import GenerateSignalPath
from hecate_v2.identify_sensitive_nodes import IdentifySensitiveNodes
from hecate_v2.netlist import Netlist
from hecate_v2.propagate_signal import FindSignalsValue

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
two_inputs = [
    {"a": 0, "b": 0},
    {"a": 0, "b": 1},
    {"a": 1, "b": 0},
    {"a": 1, "b": 1}
]
netlist = Netlist("circuit_paulo2")
netlist.read_ngspice_file()
signal_path = FindSignalsValue(netlist)

for input in all_inputs:
    print(input.get("a"), input.get("b"))
    signal_path.generate_input_values(a=input.get("a"), b=input.get("b"), c=input.get("c"))
    for output in netlist.output_signals_list:
        signal_path.find_path_from_signal(output)
    identify = IdentifySensitiveNodes(netlist.output_signals_list, netlist.intern_signals_list)
    identify.find_sensitive_nodes()
    print(input.get("a"), input.get("b"), input.get('c'), identify.sensitive_nodes)
    signal_path.reset()