import asyncio
from typing import List

from hecate.generate_inputs import GenerateInputs
from hecate.identify_sensitive_nodes import IdentifySensitiveNodes
from hecate.netlist import Netlist
from hecate.propagate_signal import FindSignalsValue
from pathlib import Path
from os.path import join as path_concat
import timeit

from hecate.signal import Signal


class Hecate:
    BASE_PATH = Path(__file__).parent

    def __init__(self, circuit_name: str):
        self.netlist = Netlist(circuit_name)
        self.circuit = circuit_name
        self.signal_path = FindSignalsValue(self.netlist)
        self.identify = IdentifySensitiveNodes(self.netlist)
        self.sensitive_nodes = []
        self.total_vectors = None
        self.evaluated_vectors = None
        self.output_values = {}
        self.reverse_biased_nodes_values = {}

    def vector_by_sensitive_node(self, node: str):
        with open(path_concat(self.BASE_PATH, "outputs", "analysis_by_node", self.circuit + ".txt"), 'w') as output:
            output.write(f"Nome do arquivo avaliado: {self.circuit} \n")
            output.write(
                f"Quantidade de vetores testados: {self.evaluated_vectors} - {self.evaluated_vectors / self.total_vectors} \n")
            output.write(f'Node {node} \n')
            for vector in self.sensitive_nodes:
                if node in vector.get('sensitive_nodes'):
                    output.write(vector.get('vector') + '\n')

    def critical_nodes(self):
        """Descobrimos em quais nodos devemos aplicar o selective hardening
             Avaliar o impacto do hardening seletivo
                -> fortalecer parte do circuito e verificar se o numero de nodos diminui
            A menor média é um circuito melhor (mais robusto/menos sensível)?
        """
        path = path_concat(self.BASE_PATH, "outputs", "critical_nodes", self.circuit + ".txt")
        with open(path, 'w') as output:
            output.write(f"Nome do arquivo avaliado: {self.circuit} \n")
            output.write(f"Quantidade de vetores testados: {self.evaluated_vectors} - {self.evaluated_vectors/self.total_vectors} \n")
            output.write(f'Node | #Vectors \n')
            # print(f'Node | #Vectors')
            sensitive_nodes = []
            for vector in self.sensitive_nodes:
                sensitive_nodes += vector.get('sensitive_nodes')
            nodes_set = set(sensitive_nodes)
            node_count = []
            for node in nodes_set:
                node_count.append((node, sensitive_nodes.count(node)))
            for node in sorted(node_count, key=lambda tup: tup[1], reverse=True):
                # print(f'{node[0]} | {node[1]}')
                output.write(f'{node[0]} | {node[1]} \n')

    def critical_vectors(self):
        """Identificamos o vetor crítico
            Comparar diferentes topologias de circuito em relação ao vetor de entrada
            Avaliar o impacto do hardening seletivo
                -> fortalecer parte do circuito e verificar se o numero de nodos diminui
            A menor média é um circuito melhor (mais robusto/menos sensível)?"""
        path = path_concat(self.BASE_PATH, "outputs", "critical_vectors", self.circuit + ".txt")
        with open(path, 'w') as output:
            # print(f'Vector | #Nodes count')
            output.write(f'Vector | #Nodes count \n')
            sensitive_nodes = []
            for vector in self.sensitive_nodes:
                sensitive_nodes.append((vector.get('vector'), len(vector.get('sensitive_nodes'))))
            for node in sorted(sensitive_nodes, key=lambda tup: tup[1], reverse=True):
                # print(f'{node[0]} | {node[1]}')
                output.write(f'{node[0]} | {node[1]} \n')

    def sensitive_nodes_for_all_input_values(self, sample_size):
        self.netlist.read_ngspice_file()
        inputs = GenerateInputs(
            inputs=self.netlist.input_signals_list
        )
        vectors, self.total_vectors, self.evaluated_vectors = inputs.get_all_input_vectors(int(sample_size))
        with open(path_concat(self.BASE_PATH, "outputs", self.circuit[:-4] + ".out"), 'w') as output:
            start = timeit.default_timer()
            output.write(f"Nome do arquivo avaliado: {self.circuit} \n")
            output.write(f"Quantidade de vetores testados: {self.evaluated_vectors} "
                         f"- {self.evaluated_vectors / self.total_vectors} \n")
            total_evaluated_nodes = len(self.netlist.intern_signals_list) + len(self.netlist.output_signals_list) + \
                                     len(self.netlist.input_signals_list)
            output.write(f"total_evaluated_nodes: {total_evaluated_nodes} \n")
            output.write('vector | sensitive_node | total_reverse_biased | not_mask_reverse_biased | runtime \n')
            for vector in vectors:
                print(vector)
                self.find_sensitive_node(vector, output)

            stop = timeit.default_timer()
            output.writelines(f'runtime: {stop - start}\n')
            print(f'runtime: {stop - start}')

    def find_sensitive_node(self, vector: dict, output):
        start = timeit.default_timer()

        self.signal_path.generate_input_values(**vector)
        self.signal_path.generate_output_values()
        self.save_outputs_value()
        self.identify.find_all_sensitive_nodes()
        self.save_reverse_biased_nodes_value(self.identify.sensitive_nodes)
        total_reverse_biased = len(self.identify.sensitive_nodes)
        # print([node.name for node in self.identify.sensitive_nodes])
        sensitive_nodes = []
        for node in self.identify.sensitive_nodes:
            self.signal_path.reset()
            self.signal_path.generate_input_values(**vector)
            if self.is_mask(node):
                continue
            sensitive_nodes.append(node.name)
        not_mask_reverse_biased = len(sensitive_nodes)
        str_vector = ''.join(str(val) for val in vector.values())
        stop = timeit.default_timer()
        self.sensitive_nodes.append({"vector": str_vector, "sensitive_nodes": sensitive_nodes})
        output.write(str_vector + " | " + str(sensitive_nodes) + " | " + str(total_reverse_biased)
                     + " | " + str(not_mask_reverse_biased) + " | " + str(stop - start) + "\n")
        self.identify.reset_sensitive_nodes()
        self.signal_path.reset()

    def sensitive_nodes_for_a_vector(self, vector: str):
        self.netlist.read_ngspice_file()
        inputs = GenerateInputs(
            inputs=self.netlist.input_signals_list
        )
        vector = inputs.get_input_vector(vector)
        start = timeit.default_timer()
        print(f"Nome do arquivo avaliado: {self.circuit}")
        print('vector | sensitive_node')

        self.signal_path.generate_input_values(**vector)
        self.signal_path.generate_output_values()
        self.save_outputs_value()

        self.identify.find_all_sensitive_nodes()
        self.save_reverse_biased_nodes_value(self.identify.sensitive_nodes)
        total_reverse_biased = len(self.identify.sensitive_nodes)
        sensitive_nodes = []
        self.signal_path.reset()
        for node in self.identify.sensitive_nodes:
            self.signal_path.reset()
            self.signal_path.generate_input_values(**vector)
            if self.is_mask(node):
                continue
            sensitive_nodes.append(node.name)
        not_mask_reverse_biased = len(sensitive_nodes)
        str_vector = ''.join(str(val) for val in vector.values())
        print({"vector": str_vector, "sensitive_nodes": sensitive_nodes})
        self.sensitive_nodes.append({"vector": str_vector, "sensitive_nodes": self.identify.sensitive_nodes})
        self.identify.reset_sensitive_nodes()
        # self.signal_path.reset()

        stop = timeit.default_timer()
        print(f'runtime: {stop - start}')

    def is_mask(self, node: Signal):
        node_value = self.reverse_biased_nodes_values[node.name]
        self.change_signal_value(node, node_value)
        self.signal_path.generate_output_values()
        return not self.is_output_different()

    def save_reverse_biased_nodes_value(self, reverse_biased_nodes: List[Signal]):
        for node in reverse_biased_nodes:
            self.reverse_biased_nodes_values[node.name] = node.get_signal_value()

    def save_outputs_value(self):
        for output in self.netlist.output_signals_list:
            self.output_values[output.name] = output.get_signal_value()

    @staticmethod
    def change_signal_value(signal: Signal, signal_value: [int, None]):
        if signal_value is None:
            return
        elif signal_value == 0:
            signal.set_signal_value(1)
        elif signal_value == 1:
            signal.set_signal_value(0)

    def is_output_different(self):
        is_different = False
        for output in self.netlist.output_signals_list:
            output_new_value = output.get_signal_value()
            output_old_value = self.output_values[output.name]
            output.reset_signal_value()
            if output_new_value != output_old_value:
                is_different = True
        return is_different




if __name__ == '__main__':
    hecate = Hecate(f"testC17_nangate")
    hecate.sensitive_nodes_for_all_input_values(1)

    # hecate.sensitive_nodes_for_a_vector("00000")
    hecate.critical_nodes()
    hecate.critical_vectors()

# salvar as saídas e dos nodos internos
# zerar o valor de todos (testar nodos reversamente polarizados)
# fixar um nodo
# ver se a saída foi alterada


"""
Probabilide amostra vetores
Circuito
total evaluated nodes
vector - total_reverse_biased - not_mask_reverse_biased - runtime
"""

