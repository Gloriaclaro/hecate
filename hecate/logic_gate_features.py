from hecate.logic_gate import LogicGate
from hecate.nangate_parser import NangateParser


class LogicGateFeatures:

    def __init__(self, circuit: str):
        self.circuit_name = f"{circuit}.v"
        self.circuit = None
        self.already_searched = {}

    def get_circuit_logic_gates(self):
        self.circuit = NangateParser(self.circuit_name)
        self.circuit.read_library()
        if self.circuit_name == 'C17_nangate.v':
            self.circuit.read_verilog_old()
        else:
            self.circuit.read_verilog_abc()

    def find_fanouts(self, gate: LogicGate):
        fanouts = 0
        for output in gate.outputs:
            if output in self.circuit.outputs:
                fanouts += 1
            for next_gate in self.circuit.logic_gate_obj:
                if next_gate.name == gate.name:
                    continue
                if output in next_gate.inputs:
                    fanouts += 1
                if output in next_gate.outputs:
                    fanouts += 1
        return fanouts

    def find_short_path(self, gate: LogicGate, distance: int = 0):
        distances = []
        for output in gate.outputs:
            if output in self.circuit.outputs:
                return distance, gate.name

            distance -= 1

            for next_gate in self.circuit.logic_gate_obj:
                if output in next_gate.inputs:
                    if next_gate.name in self.already_searched.keys():
                        # print(distance, self.already_searched[next_gate.name], next_gate.name)
                        distances.append(distance + self.already_searched[next_gate.name])
                    else:
                        new_distance, gate_name = self.find_short_path(next_gate, distance)
                        distances.append(new_distance)

        # if not distances:
        #     return "not found", gate.name
        # print(distances)
        distance = sorted(distances)[-1]
        return distance, gate.name


if __name__ == '__main__':
    lgf = LogicGateFeatures(circuit='C17_nangate')
    lgf.get_circuit_logic_gates()
    # for logic_gate in reversed(lgf.circuit.logic_gate_obj):
    #     print(logic_gate.name)
    for logic_gate in reversed(lgf.circuit.logic_gate_obj):

        distance, gate_name = lgf.find_short_path(logic_gate)
        print(distance, gate_name)
        fanouts = lgf.find_fanouts(logic_gate)
        # print(gate_name, ",", distance, ",", fanouts)

    # distance, gate_name = lgf.find_short_path(lgf.circuit.logic_gate_obj[1])
    # print(distance, gate_name)

