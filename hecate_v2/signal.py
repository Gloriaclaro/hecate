from typing import Union

from hecate_v2.transistor import Transistor


class Signal:

    def __init__(self, signal_name):
        self.name = signal_name
        self.__signal = None
        self.transistor_adj = {}

    def get_signal_value(self):
        return self.__signal

    def set_signal_value(self, signal: Union[str, int]):
        if self.get_signal_value() is None:
            self.__signal = signal

    def set_transistor_adj(self, transistor_name: str, transistor: Transistor):
        self.transistor_adj[transistor_name] = transistor