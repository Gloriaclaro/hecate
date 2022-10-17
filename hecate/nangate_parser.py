
from pathlib import Path
from os.path import join as path_concat
from typing import List

from hecate.logic_gate import LogicGate
import click

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
        self.pmos = "PMOS_VTL"
        self.nmos = "NMOS_VTL"
        self.logic_gates = {}

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
        for raw_line in verilog_lines:
            line = raw_line.strip()
            if len(line) == 0:
                continue
            raw_info = line.split(" ")

            if line.startswith('input'):
                inputs = raw_info[self.INPUTS_INDEX].replace(';', "").split(',')

            elif line.startswith('output'):
                outputs = raw_info[self.OUTPUTS_INDEX].replace(';', "").split(',')

            if line == 'endmodule':
                break

            elif is_logic_gate:
                logic_gate_pins = line[line.find('(') + 1:line.find(')')].split(",")
                logic_gate_type = raw_info[self.LOGIC_GATE_INFO_INDEX]
                logic_gate_name = raw_info[self.LOGIC_GATE_NAME_INDEX]
                logic_gate = self.logic_gates.get(logic_gate_type)
                logic_gates.append(
                    logic_gate.to_spice(
                        new_name=logic_gate_name,
                        pins=logic_gate_pins,
                    ) + '\n'
                )

            if line.startswith('wire'):
                is_logic_gate = True

        self.write_spice(logic_gates, inputs, outputs)

    def read_verilog_abc(self):
        verilog = open(self.verilog)
        verilog_lines = verilog.read()
        is_logic_gate = False
        logic_gates = []
        inputs = []
        outputs = []
        for raw_line in verilog_lines.strip().split(";"):
            line = ' '.join(raw_line.split())
            pin_info = line.replace(',', '').split()
            if pin_info[self.DESCRIPTION_INDEX] == 'input':
                inputs = pin_info[self.INPUTS_INDEX:]

            elif pin_info[self.DESCRIPTION_INDEX] == 'output':
                outputs = pin_info[self.OUTPUTS_INDEX:]

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

                logic_gates.append(
                    logic_gate.abc_to_spice(
                        new_name=logic_gate_name,
                        pins_map=pins_map,
                    ) + '\n'
                )

            if pin_info[self.DESCRIPTION_INDEX] == 'wire':
                is_logic_gate = True

        self.write_spice(logic_gates, inputs, outputs)

    def write_spice(self, logic_gates: List[LogicGate], inputs: List[str], outputs: List[str]):

        with open(path_concat(self.BASE_PATH, "circuits", "spice", self.file_name.replace('.v', '')), 'w') as output:
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

        # print(name, inputs, outputs, power, gnd)
        self.power = power
        self.gnd = gnd
        self.logic_gates[name] = LogicGate(
            name=name,
            inputs=inputs,
            outputs=outputs,
            power=power,
            gnd=gnd,
            transistors=transistors
        )


@click.command(name='verilog_to_spice')
@click.option("-n", "--name", type=str, required=True, help="Circuit verilog name")
def verilog_to_spice(name):
    parser = NangateParser(f"{name}.v")
    parser.read_library()
    parser.read_verilog_abc()

if __name__ == '__main__':
    verilog_to_spice()