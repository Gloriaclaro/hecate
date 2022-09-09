from typing import List

from hecate_v2.identify_sensitive_nodes import IdentifySensitiveNodes
from hecate_v2.netlist import Netlist
from hecate_v2.signal import Signal
from hecate_v2.transistor import Transistor


class GenerateSignalPath:
    def __init__(self, netlist: Netlist):
        self.netlist = netlist
        self.transistors_stack = []
        self.signals_control = []
        self.transistors_list_test = []

    # def find_path_from_outputs(self):
    #     outputs = self.netlist.output_signals_list
    #     for output in outputs:
    #         if output not in self.signals_control:
    #             self.signals_control.append(output)
    #         self.find_path(output)
    #         for transistor in self.transistors_stack:
    #             self.generate_path(transistor)
    #         for transistor in reversed(self.transistors_stack):
    #             self.generate_path(transistor)

    def find_path_from_output(self, output: Signal):
        if output not in self.signals_control:
            self.signals_control.append(output)
        self.find_signals_value(output)

    def generate_path(self, transistor: Transistor):
        transistor_type = transistor.get_type()
        gate = transistor.get_gate()
        gate_value = gate.get_signal_value()
        drain = transistor.get_drain()
        source = transistor.get_source()

        if gate_value is None:
            return [gate]

        if drain.get_signal_value() is None and source.get_signal_value() is None:
            return [source, drain]

        if transistor_type == self.netlist.pmos and gate_value == 0:
            self.propagate_signal(drain, source)

        if transistor_type == self.netlist.nmos and gate_value == 1:
            self.propagate_signal(drain, source)

    @staticmethod
    def propagate_signal(drain: Signal, source: Signal):
        drain_value = drain.get_signal_value()
        source_value = source.get_signal_value()

        if drain_value is not None:
            source.set_signal_value(drain_value)

        if source_value is not None:
            drain.set_signal_value(source_value)

    def find_signals_value(self, signal: Signal):
        next_transistors: List[Transistor] = signal.transistor_adj.values()
        for transistor in next_transistors:
            if transistor in self.transistors_stack:
                continue
            self.transistors_stack.insert(0, transistor)
            self.transistors_list_test.insert(0, transistor.name)
            next_signals = self.generate_path(transistor)

            print(transistor.name)

            if not next_signals:
                for transistor in self.transistors_stack:
                    self.generate_path(transistor)
                continue

            for next_signal in next_signals:
                if next_signal in self.signals_control:
                    continue
                self.signals_control.append(next_signal)
                self.find_signals_value(next_signal)

    # def find_path(self, signal: Signal):
    #     next_transistors: List[Transistor] = signal.transistor_adj.values()
    #     next_signals = []
    #     for transistor in next_transistors:
    #         if transistor in self.transistors_stack:
    #             continue
    #         self.transistors_stack.insert(0, transistor)
    #         self.transistors_list_test.insert(0, transistor.name)
    #
    #         gate = transistor.get_gate()
    #         drain = transistor.get_drain()
    #         source = transistor.get_source()
    #
    #         if gate not in next_signals:
    #             next_signals.append(gate)
    #         if drain not in next_signals:
    #             next_signals.append(drain)
    #         if source not in next_signals:
    #             next_signals.append(source)
    #
    #     for next_signal in next_signals:
    #         if next_signal in self.signals_control:
    #             continue
    #         self.signals_control.append(next_signal)
    #         self.find_path(next_signal)

    # def find_path(self, signal: Signal):
    #     next_transistors: List[Transistor] = signal.transistor_adj.values()
    #     for transistor in next_transistors:
    #         next_signal = None
    #         if transistor in self.transistors_stack:
    #             continue
    #         gate = transistor.get_gate()
    #         drain = transistor.get_drain()
    #         source = transistor.get_source()
    #         if source == signal:
    #             next_signal = drain
    #         if drain == signal:
    #             next_signal = source
    #         if gate == signal:
    #             next_signal = gate
    #         self.transistors_stack.insert(0, transistor)
    #         if not next_signal:
    #             continue
    #         self.find_path(next_signal)

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