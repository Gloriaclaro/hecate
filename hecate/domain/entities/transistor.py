from abc import ABC, abstractmethod
from enum import Enum


class TransistorIndex(Enum):
    TRANSISTOR_NAME = 0
    SOURCE_SIGNAL_NAME = 1
    GATE_SIGNAL_NAME = 2
    DRAIN_SIGNAL_NAME = 3
    BULK_SIGNAL_NAME = 4
    NODE_TYPE = 5


class Transistor(ABC):
    def __init__(self, transistor_info: list):
        self.__info: list = transistor_info

    def get_transistor_name(self):
        return self.__info[TransistorIndex.TRANSISTOR_NAME.value]

    def get_source_name(self):
        return self.__info[TransistorIndex.SOURCE_SIGNAL_NAME.value]

    def get_gate_name(self):
        return self.__info[TransistorIndex.GATE_SIGNAL_NAME.value]

    def get_drain_name(self):
        return self.__info[TransistorIndex.DRAIN_SIGNAL_NAME.value]

    def get_bulk_name(self):
        return self.__info[TransistorIndex.BULK_SIGNAL_NAME.value]

    def get_type(self):
        return self.__info[TransistorIndex.NODE_TYPE.value]

