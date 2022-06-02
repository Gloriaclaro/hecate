from typing import Union

from hecate.domain.abstract.signal import Signal


class NSignal(Signal):

    def set_edge_signal(self, last_signal: Union[str, int], node: str, next_node: str, circuit):
        if circuit.nodes[node]["signal"].get_signal_value() == 1:
            circuit[node][next_node]["signal"].set_signal_value(last_signal)
            circuit[node][next_node]['value'] = last_signal
        else:
            last_signal = 'x'
            circuit[node][next_node]['value'] = last_signal
        return last_signal
