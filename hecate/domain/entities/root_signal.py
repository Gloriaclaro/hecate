from hecate.domain.abstract.signal import Signal
from typing import Union


class RootSignal(Signal):

    def __init__(self, signal_name: str, signal: int):
        super().__init__(signal_name)
        self.__signal = signal

    def set_edge_signal(self, last_signal: Union[str, int], node: str, next_node: str, circuit):
        if circuit.nodes[next_node]["signal"].get_signal_value() == 'x':
            circuit.nodes[next_node]["signal"].set_signal_value(last_signal)
        circuit[node][next_node]["signal"].set_signal_value(last_signal)
        circuit[node][next_node]['value'] = last_signal
        return last_signal
