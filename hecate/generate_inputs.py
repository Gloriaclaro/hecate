from typing import List

from hecate.signal import Signal


class GenerateInputs:

    def __init__(self, inputs: List[Signal]):
        self._inputs = inputs
        self._inputs_name_list = self.get_inputs_names()

    def get_all_input_vectors(self):
        vectors = []
        length = len(self._inputs)
        for i in range(2 ** length):
            vector = bin(i)[2:].zfill(length)
            binaries = map(int, list(vector))
            vectors_input_name = dict(zip(self._inputs_name_list, binaries))
            vectors.append(vectors_input_name)
            if i == 2:
                return vectors
        return vectors

    def get_inputs_names(self):
        return [input.name for input in self._inputs]


