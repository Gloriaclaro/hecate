from abc import ABC, abstractmethod
from typing import Union


class Signal(ABC):

    def __init__(self, signal_name):
        self.__name = signal_name
        self.__signal = 'x'

    def get_signal_name(self):
        return self.__name

    def get_signal_value(self):
        return self.__signal

    def set_signal_value(self, signal: Union[str, int]):
        self.__signal = signal

    @abstractmethod
    def set_edge_signal(self, last_signal: Union[str, int], node: str, next_node: str, circuit):
        ...
