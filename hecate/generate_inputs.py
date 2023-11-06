import random
from typing import List

from hecate.signal import Signal


class GenerateInputs:

    def __init__(self, inputs: List[Signal]):
        self._inputs = inputs
        self._inputs_name_list = self.get_inputs_names()

    def get_input_vector(self, vector: str):
        binaries = map(int, list(vector))
        return dict(zip(self._inputs_name_list, binaries))

    def get_all_input_vectors(self, sample_size: int) -> tuple:
        length = len(self._inputs)
        # if 2**length < sample_size:
        # vectors = self.get_seq_input_vectors(sample_size)
        vectors = self.get_seq_input_vectors(2**length)
        # else:
        #     vectors = self.get_random_input_vectors(sample_size)
        return vectors,  2 ** length, len(vectors)

    def get_seq_input_vectors(self, sample_size: int) -> list:
        vectors = []
        length = len(self._inputs)
        for i in range(0, 2 ** length):
            vector = bin(i)[2:].zfill(length)
            binaries = map(int, list(vector))
            vectors_input_name = dict(zip(self._inputs_name_list, binaries))
            vectors.append(vectors_input_name)
            if i > sample_size:
                break
        return vectors

    def get_random_input_vectors(self, sample_size: int) -> list:
        vectors = []
        length = len(self._inputs)
        for i in range(1, 2 ** length):
            if i > sample_size:
                break
            vector = bin(random.randint(0, 2 ** length))[2:].zfill(length)
            binaries = map(int, list(vector))
            vectors_input_name = dict(zip(self._inputs_name_list, binaries))
            vectors.append(vectors_input_name)

        return vectors

    def get_inputs_names(self):
        return [input.name for input in self._inputs]


