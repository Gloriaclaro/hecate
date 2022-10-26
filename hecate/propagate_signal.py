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
        same_values = []
        for output in self.netlist.output_signals_list:
            same_values.append(self.find_path_from_signal(output))
        return all(same_values)

    def find_path_from_signal(self, signal: Signal):
        value, signals_list = self.find_signals_value(signal, [])
        self.set_signals_value(value, signals_list)
        values = []
        for signal in signals_list:
            values.append(signal.get_signal_value())
        return all(values)

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