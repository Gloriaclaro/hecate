from typing import Union
from hecate.domain.abstract.signal import Signal


class MiddleSignal(Signal):

    def __init__(self, bulk: int, signal_name):
        super().__init__(signal_name)
        self.__bulk = bulk

    def get_signal_bulk(self):
        return self.__bulk

    def set_edge_signal(self, last_signal: Union[str, int], node: str, next_node: str, circuit):
        if circuit.nodes[node]["signal"].get_signal_value() == 'x':
            circuit.nodes[node]["signal"].set_signal_value(last_signal)
        circuit[node][next_node]["signal"].set_signal_value(last_signal)
        circuit[node][next_node]['value'] = last_signal
        return last_signal

