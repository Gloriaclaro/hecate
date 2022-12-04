from pathlib import Path
from os.path import join as path_concat

from hecate.signal import Signal
from hecate.transistor import Transistor


class Netlist:
    WITHOUT_GATE = -1
    BASE_PATH = Path(__file__).parent
    SIGNALS_NAME_INDEX = 1
    SIGNAL_DESCRIPTION_INDEX = 0
    TRANSISTOR_NAME = 0
    DRAIN_SIGNAL_NAME = 1
    GATE_SIGNAL_NAME = 2
    SOURCE_SIGNAL_NAME = 3
    BULK_SIGNAL_NAME = 4
    TRANSISTOR_TYPE = 5

    def __init__(self,  file_name: str):
        self.file_path = path_concat(self.BASE_PATH, "circuits", "spice", file_name)
        self.pmos = []
        self.nmos = []
        self.transistors = {}
        self.signals = {}
        self.input_signals_list = []
        self.output_signals_list = []
        self.power_signals_list = []
        self.intern_signals_list = []

    def read_ngspice_file(self):
        file = open(self.file_path)
        file_lines = file.readlines()
        transistor_index = 0

        for i in range(len(file_lines)):
            if file_lines[i].startswith('.'):
                continue
            transistor_index = i
            break

        metadata_lines = file_lines[:transistor_index]
        transistors_list = file_lines[transistor_index:]

        self._read_metadata_and_create_signals(metadata_lines)
        self._create_transistors(transistors_list)

    def _read_metadata_and_create_signals(self, metadata_lines: list):
        for line in metadata_lines:
            line_list = line.strip().split(" ")
            description = line_list[self.SIGNAL_DESCRIPTION_INDEX]
            names = line_list[self.SIGNALS_NAME_INDEX:]
            if "supply" in description:
                for name in names:
                    signal = self.create_signal(name)
                    signal.set_signal_value(1)
                    self.power_signals_list.append(signal)

            if "ground" in description:
                for name in names:
                    signal = self.create_signal(name)
                    signal.set_signal_value(0)
                    self.power_signals_list.append(signal)

            if "inputs" in description:
                for name in names:
                    signal = self.create_signal(name)
                    self.input_signals_list.append(signal)

            if "outputs" in description:
                for name in names:
                    signal = self.create_signal(name)
                    self.output_signals_list.append(signal)

            if "P-Type" in description:
                self.pmos = names

            if "N-Type" in description:
                self.nmos = names

    def create_signal(self, name: str):
        signal = Signal(name)
        self.signals[name] = signal
        return signal

    def _create_transistors(self, transistors_list: list):
        for line in transistors_list:
            transistor_info = line.strip().split(" ")
            if len(transistor_info) < 5:
                continue
            name = transistor_info[self.TRANSISTOR_NAME]
            drain = transistor_info[self.DRAIN_SIGNAL_NAME]
            gate = transistor_info[self.GATE_SIGNAL_NAME]
            source = transistor_info[self.SOURCE_SIGNAL_NAME]
            bulk = Signal(transistor_info[self.BULK_SIGNAL_NAME])
            transistor_type = transistor_info[self.TRANSISTOR_TYPE]
            self.set_bulk_value(bulk, transistor_type)
            signals = self.get_or_create_signal([drain, source, gate], name)
            transistor = Transistor(name, *signals, bulk, transistor_type)
            self.set_transistor_adj(name, transistor, signals)
            self.transistors[name] = transistor

    def set_bulk_value(self, bulk: Signal, transistor_type: str):
        if transistor_type in self.pmos:
            bulk.set_signal_value(1)
        if transistor_type in self.nmos:
            bulk.set_signal_value(0)

    def get_or_create_signal(self, signals_name: list, transistor_name: str):
        signals = []
        for name in signals_name:
            signal = self.signals.get(name)

            if not signal:
                signal = self.create_signal(name)
                self.intern_signals_list.append(signal)
            signals.append(signal)

        return signals

    def set_transistor_adj(self, transistor_name: str, transistor: Transistor, signals: list):
        signals = signals[:self.WITHOUT_GATE]
        for signal in signals:
            signal.set_transistor_adj(transistor_name, transistor)