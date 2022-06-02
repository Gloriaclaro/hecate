from typing import Union
from hecate.domain.abstract.signal import Signal


class MiddleSignal(Signal):

    def set_edge_signal(self, last_signal: Union[str, int], node: str, next_node: str, circuit):
        if circuit.nodes[next_node]["signal"].get_signal_value() == 'x':
            circuit.nodes[next_node]["signal"].set_signal_value(last_signal)
        circuit[node][next_node]["signal"].set_signal_value(last_signal)
        circuit[node][next_node]['value'] = last_signal
        return last_signal

