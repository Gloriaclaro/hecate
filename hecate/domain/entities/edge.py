class EdgeSignal:

    def __init__(self):
        self.__signal = 'x'

    def get_signal_value(self):
        return self.__signal

    def set_signal_value(self, signal):
        self.__signal = signal

