
from pathlib import Path
from os.path import join as path_concat
from typing import List

from hecate.logic_gate import LogicGate


class NangateParser:
    BASE_PATH = Path(__file__).parent
    DESCRIPTION_INDEX = 0
    PIN_INFO_INDEX = 1
    PIN_DESCRIPTION_INDEX = 1
    INPUTS_INDEX = 1
    OUTPUTS_INDEX = 1
    PIN_NAME = 0
    TRANSISTOR_INDEX = 3
    LOGIC_GATE_NAME_INDEX = 1
    LOGIC_GATE_INFO_INDEX = 0

    def __init__(self,  file_name: str, library: str = "NangateLibrary.spi"):
        self.file_name = file_name
        self.verilog = path_concat(self.BASE_PATH, "circuits", "verilog", file_name)
        self.library = path_concat(self.BASE_PATH, "circuits", "library", library)
        self.power = None
        self.gnd = None
        self.outputs = []
        self.inputs = []
        self.pmos = "PMOS_VTL PMOS_VTH"
        self.nmos = "NMOS_VTL NMOS_VTH NMOS_NT"
        self.logic_gates = {}
        self.logic_gate_obj = []

    def read_library(self):
        library = open(self.library)
        library_lines = library.readlines()

        logic_gate_info = []
        is_logic_gate_info = False

        for index, line in enumerate(library_lines):

            if line.startswith('.SUBCKT'):
                is_logic_gate_info = True

            if line.startswith('.ENDS'):
                is_logic_gate_info = False
                self.create_logic_gate(logic_gate_info)
                logic_gate_info = []

            if is_logic_gate_info:
                logic_gate_info.append(line.strip())

    def read_verilog_old(self):
        verilog = open(self.verilog)
        verilog_lines = verilog.readlines()
        is_logic_gate = False
        logic_gates = []
        inputs = []
        outputs = []
        with open(path_concat(self.BASE_PATH, "circuits", "logic_gate", "test"+self.file_name.replace('.v', '')), 'w') as output:
            output.write('logic_gate nodes' + "\n")
            for raw_line in verilog_lines:
                line = raw_line.strip()
                if len(line) == 0 or line == "\n":
                    continue

                raw_info = line.split(" ")

                if line.startswith('input'):
                    inputs = raw_info[self.INPUTS_INDEX].replace(';', "").split(',')
                    self.inputs = inputs

                elif line.startswith('output'):
                    outputs = raw_info[self.OUTPUTS_INDEX].replace(';', "").split(',')
                    self.outputs = outputs

                if line == 'endmodule':
                    break

                elif is_logic_gate:
                    logic_gate_pins = line[line.find('(') + 1:line.find(')')].split(",")
                    logic_gate_type = raw_info[self.LOGIC_GATE_INFO_INDEX]
                    logic_gate_name = raw_info[self.LOGIC_GATE_NAME_INDEX]

                    logic_gate = self.logic_gates.get(logic_gate_type)

                    transistor_info, inputs, outputs, others = logic_gate.to_spice(
                            new_name=logic_gate_name,
                            pins=logic_gate_pins,
                        )
                    logic_gates.append(
                        transistor_info + '\n'
                    )
                    self.logic_gate_obj.append(
                        LogicGate(
                            name=logic_gate_name,
                            inputs=inputs,
                            outputs=outputs,
                            power="power",
                            gnd="gnd",
                            transistors=[],
                            file_name=self.file_name
                        ))
                    output.write(logic_gate_name.strip() + " ")
                    output.write(",".join(outputs) + "\n")

                if line.startswith('wire'):
                    is_logic_gate = True

        self.write_spice(logic_gates, self.inputs, self.outputs)

    def read_verilog_abc(self):
        verilog = open(self.verilog)
        verilog_lines = verilog.read()
        is_logic_gate = False
        logic_gates = []
        with open(path_concat(self.BASE_PATH, "circuits", "logic_gate", self.file_name.replace('.v', '')), 'w') as output:
            output.write('logic_gate nodes' + "\n")
            for raw_line in verilog_lines.strip().split(";"):
                line = ' '.join(raw_line.split())
                pin_info = line.replace(',', '').split()
                if pin_info[self.DESCRIPTION_INDEX] == 'input':
                    inputs = pin_info[self.INPUTS_INDEX:]
                    self.inputs = inputs

                elif pin_info[self.DESCRIPTION_INDEX] == 'output':
                    outputs = pin_info[self.OUTPUTS_INDEX:]
                    self.outputs = outputs

                if line.startswith('endmodule'):
                    break

                elif is_logic_gate:
                    logic_gate_type = pin_info[self.LOGIC_GATE_INFO_INDEX]
                    pin_info = " ".join(pin_info[self.LOGIC_GATE_NAME_INDEX:])
                    logic_gate_pins = pin_info.replace(')', "(").replace('.', '').strip().split('(')
                    logic_gate_name = logic_gate_pins[self.LOGIC_GATE_INFO_INDEX]
                    pin_info = logic_gate_pins[self.LOGIC_GATE_NAME_INDEX:-2]
                    pins_map = {}
                    for i in range(0, len(pin_info), 2):
                        pins_map[pin_info[i].strip()] = pin_info[i+1].strip()

                    logic_gate = self.logic_gates.get(logic_gate_type)
                    transistor_info, inputs, outputs, nodes = logic_gate.abc_to_spice(
                            new_name=logic_gate_name,
                            pins_map=pins_map,
                        )
                    # print(inputs, outputs, nodes, logic_gate_name)
                    logic_gates.append(
                        transistor_info + '\n'
                    )
                    self.logic_gate_obj.append(
                        LogicGate(
                            name=logic_gate_name,
                            inputs=inputs,
                            outputs=outputs,
                            power="power",
                            gnd="gnd",
                            transistors=[],
                            file_name=self.file_name
                        ))
                    output.write(logic_gate_name.strip() + " ")
                    # output.write(",".join(inputs) + "\n")
                    output.write(",".join(outputs+nodes) + "\n")
                if pin_info[self.DESCRIPTION_INDEX] == 'wire':
                    is_logic_gate = True

        self.write_spice(logic_gates, self.inputs, self.outputs)

    def write_spice(self, logic_gates: List[LogicGate], inputs: List[str], outputs: List[str]):

        with open(path_concat(self.BASE_PATH, "circuits", "spice", "test" + self.file_name.replace('.v', '')), 'w') as output:
            output.write(f".supply {self.power} \n")
            output.write(f".ground {self.gnd} \n")
            output.write(f".P-Type {self.pmos} \n")
            output.write(f".N-Type {self.nmos} \n")
            output.write(f".inputs {' '.join(inputs)}\n")
            output.write(f".outputs {' '.join(outputs)}\n\n")
            output.writelines(logic_gates)

    def create_logic_gate(self, logic_gate_info: List[str]):
        metadata = logic_gate_info[:self.TRANSISTOR_INDEX]
        transistors = logic_gate_info[self.TRANSISTOR_INDEX:]
        inputs = []
        outputs = []
        power = None
        gnd = None
        name = metadata[self.LOGIC_GATE_INFO_INDEX].split(" ")[self.LOGIC_GATE_NAME_INDEX]
        raw_pin_info = metadata[self.PIN_INFO_INDEX].split(" ")

        for raw_info in raw_pin_info[self.PIN_INFO_INDEX:]:
            info = raw_info.split(':')
            description = info[self.PIN_DESCRIPTION_INDEX]
            pin_name = info[self.PIN_NAME]
            if description == 'I':
                inputs.append(pin_name)
            if description == 'O':
                outputs.append(pin_name)
            if description == 'P':
                power = pin_name
            if description == 'G':
                gnd = pin_name

        self.power = power
        self.gnd = gnd

        self.logic_gates[name] = LogicGate(
            name=name,
            inputs=inputs,
            outputs=outputs,
            power=power,
            gnd=gnd,
            transistors=transistors,
            file_name=self.file_name
        )


# @click.command(name='verilog_to_spice')
# @click.option("-n", "--name", type=str, required=True, help="Circuit verilog name")
def verilog_to_spice(name):
    for circuit in ['C17_nangate']:
        parser = NangateParser(f"{circuit}.v")
        parser.read_library()
        parser.read_verilog_old()
    # for circuit in ['c432', 'c499', 'c880', 'c1355', 'c1908',
    #                     'c2670', 'c3540', 'c5315', 'c6288', 'c7552']:
    #     parser = NangateParser(f"{circuit}.v")
    #     parser.read_library()
    #     parser.read_verilog_abc()

if __name__ == '__main__':
    verilog_to_spice('C17_nangate')