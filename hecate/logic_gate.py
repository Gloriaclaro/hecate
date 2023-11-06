from typing import List
from pathlib import Path
from os.path import join as path_concat


class LogicGate:
    TRANSISTOR_NAME_INDEX = 0
    PIN_START = 1
    PIN_END = 4
    BASE_PATH = Path(__file__).parent

    def __init__(self, name: str, inputs: List[str], outputs: List[str], power: str, gnd: str, transistors: List[str], file_name: str):
        self.file_name = file_name
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.power = power
        self.gnd = gnd
        self.transistors = transistors

    def get_logic_gate_name(self):
        return self.name

    def get_inputs_list(self):
        return self.inputs

    def get_outputs_list(self):
        return self.outputs

    def get_power_name(self):
        return self.power

    def get_gnd_name(self):
        return self.gnd

    def get_transistors_list(self):
        return self.transistors

    def to_spice(self, new_name: str, pins: List[str]):
        transistors_spice = ""
        outputs_length = len(self.outputs)
        new_outputs = pins[:outputs_length]
        new_inputs = pins[outputs_length:]
        nodes = []
        inputs = []
        outputs = []
        for transistor in self.transistors:
            raw_transistor = transistor.split(' ')
            transistor = raw_transistor[self.TRANSISTOR_NAME_INDEX] + "_" + new_name + " "
            for pin in raw_transistor[self.PIN_START:self.PIN_END]:
                if pin in self.inputs:
                    new_input = new_inputs[self.inputs.index(pin)].strip()
                    if new_input not in inputs:
                        inputs.append(new_input)
                    transistor = transistor + new_inputs[self.inputs.index(pin)].strip() + " "
                elif pin in self.outputs:
                    new_output = new_outputs[self.outputs.index(pin)].strip()
                    if new_output not in outputs:
                        outputs.append(new_outputs[self.outputs.index(pin)].strip())
                    transistor = transistor + new_outputs[self.outputs.index(pin)].strip() + " "
                elif pin == self.power or pin == self.gnd:
                    transistor = transistor + pin.strip() + " "
                else:
                    if pin.strip() + "_" + new_name.strip() not in nodes:
                        nodes.append(pin.strip() + "_" + new_name.strip())
                    transistor = transistor + pin.strip() + "_" + new_name.strip() + " "
            transistor = transistor + " ".join(raw_transistor[self.PIN_END:])
            transistors_spice = transistors_spice + transistor + "\n"
        return transistors_spice, inputs, outputs, nodes

    def abc_to_spice(self, new_name: str, pins_map: dict):
        transistors_spice = ""
        inputs = []
        outputs = []
        nodes = []
        for transistor in self.transistors:
            raw_transistor = transistor.split(' ')
            transistor = raw_transistor[self.TRANSISTOR_NAME_INDEX] + "_" + new_name + " "
            for pin in raw_transistor[self.PIN_START:self.PIN_END]:
                if (pin in self.inputs) and (pins_map[pin] not in inputs):
                    inputs.append(pins_map[pin])

                if (pin in self.outputs) and (pins_map[pin] not in outputs):
                    outputs.append(pins_map[pin])

                if pin in pins_map.keys():
                    transistor = transistor + pins_map[pin] + " "

                elif pin == self.power or pin == self.gnd:
                    transistor = transistor + pin.strip() + " "

                else:
                    if (pin.strip() + "_" + new_name.strip()) not in nodes:
                        nodes.append(pin.strip() + "_" + new_name.strip())
                    transistor = transistor + pin.strip() + "_" + new_name.strip() + " "
            transistor = transistor + " ".join(raw_transistor[self.PIN_END:])
            transistors_spice = transistors_spice + transistor + "\n"
        return transistors_spice, inputs, outputs, nodes

    #
    # def abc_to_spice(self, new_name: str, pins_map: dict):
    #     transistors_spice = ""
    #     nodes = []
    #     inputs = []
    #     outputs = []
    #     for transistor in self.transistors:
    #         raw_transistor = transistor.split(' ')
    #         transistor = raw_transistor[self.TRANSISTOR_NAME_INDEX] + "_" + new_name + " "
    #         for pin in raw_transistor[self.PIN_START:self.PIN_END]:
    #             if pin in pins_map.keys():
    #                 transistor = transistor + pins_map[pin] + " "
    #                 if pins_map[pin] not in nodes:
    #                     if (pin in self.inputs) and (pins_map[pin] not in inputs):
    #                         inputs.append(pins_map[pin])
    #                     if (pin in self.outputs) and (pins_map[pin] not in outputs):
    #                         outputs.append(pins_map[pin])
    #             elif pin == self.power or pin == self.gnd:
    #                 transistor = transistor + pin.strip() + " "
    #             else:
    #                 if (pin.strip() + "_" + new_name.strip())not in nodes:
    #                     nodes.append(pin.strip() + "_" + new_name.strip())
    #                 transistor = transistor + pin.strip() + "_" + new_name.strip() + " "
    #         transistor = transistor + " ".join(raw_transistor[self.PIN_END:])
    #         transistors_spice = transistors_spice + transistor + "\n"
    #     return transistors_spice, inputs, outputs, nodes