from typing import List
from hecate.netlist import Netlist
from hecate.signal import Signal
from hecate.transistor import Transistor


class FindSignalsValue:
    def __init__(self, netlist: Netlist):
        self.netlist = netlist
        self.transistors_stack = []
        self.signals_control = []
        self.transistors_list_test = []
        self._signals_control = []

    def generate_output_values(self):
        for output in self.netlist.output_signals_list:
            self.find_path_from_signal(output)

    def find_path_from_signal(self, signal: Signal):
        value, signals_list = self.find_signals_value(signal, [])
        test_list = []

        self.set_signals_value(value, signals_list)
        for signal in signals_list:
            test_list.append(str(signal.get_signal_value()))
        if not len(set(test_list)) == 1:
            self.change_signal_value(signal, value)

    def find_signals_value(self, signal: Signal, signals_list: [Signal]):
        next_transistors: List[Transistor] = signal.transistor_adj.values()
        value = None
        for transistor in next_transistors:
            gate = transistor.get_gate()
            drain = transistor.get_drain()
            source = transistor.get_source()
            gate_value = gate.get_signal_value()

            if gate_value is None:
                self.find_path_from_signal(gate)

            there_is_path = self.find_path(transistor, gate)

            if not there_is_path:
                continue

            if drain in self.netlist.power_signals_list or drain in self.netlist.input_signals_list:
                value = drain.get_signal_value()

            elif drain not in signals_list:
                signals_list.append(drain)
                aux_value = value
                if drain not in self.netlist.output_signals_list:
                    value, signals_list = self.find_signals_value(drain, signals_list)
                    if value is None:
                        value = aux_value

            if source in self.netlist.power_signals_list or source in self.netlist.input_signals_list:
                value = source.get_signal_value()

            elif source not in signals_list:
                signals_list.append(source)
                aux_value = value
                if source not in self.netlist.output_signals_list:
                    value, signals_list = self.find_signals_value(source, signals_list)
                    if value is None:
                        value = aux_value

        return value, signals_list

    def find_path(self, transistor: Transistor, gate: Signal):
        gate_value = gate.get_signal_value()
        there_is_a_path = False
        transistor_type = transistor.get_type()
        if transistor_type == self.netlist.pmos and gate_value == 0:
            there_is_a_path = True

        if transistor_type == self.netlist.nmos and gate_value == 1:
            there_is_a_path = True

        return there_is_a_path

    def set_signals_value(self, value: int, signals_list: [Signal]):
        for signal in signals_list:
            signal.set_signal_value(value)

    @staticmethod
    def change_signal_value(signal: Signal, signal_value: [int, None]):
        signal.reset_signal_value()
        if signal_value == 0:
            signal.set_signal_value(1)
        elif signal_value == 1:
            signal.set_signal_value(0)

    def reset(self):
        signals_to_reset = [
            *self.netlist.input_signals_list,
            *self.netlist.output_signals_list,
            *self.netlist.intern_signals_list
        ]
        for signal in signals_to_reset:
            signal.reset_signal_value()
        self.transistors_stack = []
        self.signals_control = []

    def set_inputs_high(self):
        for input_signal in self.netlist.input_signals_list:
            input_signal.set_signal_value(1)

    def set_inputs_low(self):
        for input_signal in self.netlist.input_signals_list:
            input_signal.set_signal_value(0)

    def set_inputs_value(self):
        for input_signal in self.netlist.input_signals_list:
            value = int(input(input_signal.name + ":"))
            input_signal.set_signal_value(value)

    def generate_input_values(self, **kwargs):
        for input_signal in self.netlist.input_signals_list:
            value = kwargs.get(input_signal.name)
            input_signal.set_signal_value(value)