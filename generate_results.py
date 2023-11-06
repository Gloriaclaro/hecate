import math
from pathlib import Path
from os.path import join as path_concat
import pandas as pd

from hecate.logic_gate_features import LogicGateFeatures


class GenerateResults:
    BASE_PATH = Path(__file__).parent

    def __init__(self, file_name: str):
        self.critical_nodes_path = path_concat(self.BASE_PATH, "outputs", "temp", "100", "critical_nodes")
        self.critical_vectors_path = path_concat(self.BASE_PATH, "outputs", "temp", "100", "critical_vectors")
        self.full_result_path_100 = path_concat(self.BASE_PATH, "outputs", "temp", "100")
        self.full_result_path_400 = path_concat(self.BASE_PATH, "outputs", "temp", "400")
        self.logic_gates_path = path_concat(self.BASE_PATH, "hecate", "circuits", "logic_gate")
        self.vectors_average = 0
        self.nodes_average = 0
        self.critical_nodes = 0

    def get_runtime(self):
        run_100 = []
        run_400 = []
        for circuit in ['c17', 'c432.txt', 'c499.txt', 'c880.txt', 'c1355.txt', 'c1908.txt',
                        'c2670.txt', 'c3540.txt', 'c5315.txt', 'c6288.txt', 'c7552.txt']:
            library_100 = open(path_concat(self.full_result_path_100, circuit))
            library_lines_100 = library_100.readlines()
            library = open(path_concat(self.full_result_path_400, circuit))
            library_lines = library.readlines()
            print(library_lines_100[-1].split(":")[1].strip().replace('.', ','))
            # print(library_lines[-1].split(":")[1].strip().replace('.', ','))

            run_100.append(library_lines_100[-1].split(":")[1].strip())

            run_400.append(library_lines[-1].split(":")[1].strip())

    def get_critical_nodes(self, circuit):
        library = open(path_concat(self.critical_nodes_path, circuit))
        library_lines = library.readlines()

        nodes = {}

        for index, line in enumerate(library_lines):
            if index < 3:
                continue
            nodes[line.strip().split('|')[0].strip()] = line.strip().split('|')[1].strip()

        return nodes

    def critical_nodes_average(self):
        for circuit in ['c17', 'c432.txt', 'c499.txt', 'c880.txt', 'c1355.txt', 'c1908.txt',
                        'c2670.txt', 'c3540.txt', 'c5315.txt', 'c6288.txt', 'c7552.txt']:

            library = open(path_concat(self.critical_nodes_path, circuit))
            library_lines = library.readlines()

            vectors = 0
            length = 0

            for index, line in enumerate(library_lines):
                if index < 3:
                    continue
                vectors = vectors + int(line.strip().split('|')[1])
                length += 1

            self.vectors_average = vectors / length
            # print(str(round(self.vectors_average, 2)).replace('.', ','), end=" ")
            self.nodes_above_average(circuit)

    def nodes_above_average(self, circuit):
        library = open(path_concat(self.critical_nodes_path, circuit))
        library_lines = library.readlines()

        critical_nodes = 0

        for index, line in enumerate(library_lines):

            if index < 3:
                continue

            if int(line.strip().split('|')[1]) > self.vectors_average:
                critical_nodes += 1

        self.critical_nodes = critical_nodes
        print(self.critical_nodes)

    def critical_vectors_average(self):
        for circuit in ['c17', 'c432.txt', 'c499.txt', 'c880.txt', 'c1355.txt', 'c1908.txt',
                        'c2670.txt', 'c3540.txt', 'c5315.txt', 'c6288.txt', 'c7552.txt']:

            library = open(path_concat(self.critical_vectors_path, circuit))
            library_lines = library.readlines()

            nodes = 0
            length = 0

            for index, line in enumerate(library_lines):
                if index == 0:
                    continue
                nodes = nodes + int(line.strip().split('|')[1])
                length += 1
            self.nodes_average = nodes / length
            print(str(round(self.nodes_average, 2)).replace('.', ','))

    def get_circuit_logic_gates(self, circuit):
        library = open(path_concat(self.logic_gates_path, circuit))
        library_lines = library.readlines()

        logic_gates_node_map = {}

        for index, line in enumerate(library_lines):
            if index == 0:
                continue
            logic_gates_node_map[line.split(" ")[0]] = line.split(" ")[1].strip().split(",")

        return logic_gates_node_map

    def get_vectors_by_deep_and_fanout(self, circuit: str) -> list:
        logic_gate_features = []
        lgf = LogicGateFeatures(circuit=circuit.replace('.txt', ''))
        lgf.get_circuit_logic_gates()
        for logic_gate in reversed(lgf.circuit.logic_gate_obj):
            distance, gate_name = lgf.find_short_path(logic_gate)
            lgf.already_searched[gate_name] = distance
            fanouts = lgf.find_fanouts(logic_gate)
            logic_gate_features.append({
                "logic_gate": gate_name,
                "Deep": distance,
                "Fanouts": fanouts
            })
        return logic_gate_features

    def get_vectors_by_max_and_sum_of_vectors(self, circuit) -> pd.DataFrame:
        logic_gate_critical_nodes = []
        critical_nodes = self.get_critical_nodes(circuit)
        logic_gates = self.get_circuit_logic_gates(circuit.replace('.txt', ''))
        for critical_node in critical_nodes.keys():
            for logic_gate in logic_gates.keys():
                if critical_node in logic_gates[logic_gate]:
                    logic_gate_critical_nodes.append(
                        {"logic_gate": logic_gate,
                         "number_vectors": int(critical_nodes[critical_node]),
                         })
        df = pd.DataFrame(logic_gate_critical_nodes)
        sum_max_vectors_by_gate = df.groupby('logic_gate')['number_vectors'].agg(("max", "unique", "sum")).reset_index()
        sum_max_vectors_by_gate['sum-max'] = sum_max_vectors_by_gate.apply(lambda x: (x['sum'] - x['max']), axis=1)

        return sum_max_vectors_by_gate

    def get_logic_gate_critical_nodes(self):
        for circuit in ['c432.txt', 'c499.txt', 'c880.txt', 'c1355.txt', 'c1908.txt',
                         'c3540.txt', 'c5315.txt', 'c6288.txt', 'c7552.txt']:
            print(circuit)
            sum_max_vectors_by_gate = self.get_vectors_by_max_and_sum_of_vectors(circuit)

            sum_max_vectors_by_gate.sort_values(['max', 'sum-max'], ascending=False, inplace=True)
            total = sum_max_vectors_by_gate['sum'].sum()

            logic_gate_features = self.get_vectors_by_deep_and_fanout(circuit)
            features_df = pd.DataFrame(logic_gate_features)
            resulted_df = pd.merge(sum_max_vectors_by_gate, features_df, on='logic_gate')

            resulted_df.sort_values(['Deep', 'Fanouts'], ascending=False, inplace=True)

            n_gates = len(sum_max_vectors_by_gate)
            selective_hardening_output = {
                "circuit": circuit,
                "total": total,
                "results": []
            }
            for percentage in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]:
                selected_gates_number = math.ceil(n_gates*percentage)

                total_selected = sum_max_vectors_by_gate.head(selected_gates_number)['sum'].sum()
                deep_fanouts_total_selected = resulted_df.head(selected_gates_number)['sum'].sum()

                total_remaining = sum_max_vectors_by_gate.iloc[selected_gates_number:]['sum'].sum()
                deep_fanouts_total_remaining = resulted_df.iloc[selected_gates_number:]['sum'].sum()
                selective_hardening_output['results'].append(
                    {
                        "percentage": percentage,
                        "selected_gates": selected_gates_number,
                        "difference": total_selected - deep_fanouts_total_selected,
                        "max_sum_total_vectors_for_selected_gates": total_selected,
                        "max_sum_total_vectors_remaining_gates": total_remaining,
                        "deep_fanout_total_vectors_for_selected_gates": deep_fanouts_total_selected,
                        "deep_fanout_total_vectors_remaining_gates": deep_fanouts_total_remaining,
                    }
                )
            results_df = pd.DataFrame(selective_hardening_output['results'])
            results_df.to_csv(path_concat(self.BASE_PATH, "outputs", "max_sum_vs_deep_fanout", circuit))

            resulted_df.to_csv(path_concat(self.BASE_PATH, "outputs", "sensitive_nodes_by_logic_gate", circuit))

    def get_new_sus(self):
        for circuit in ['c17']:
            critical_nodes = self.get_critical_nodes(circuit)
            library = open(path_concat(self.full_result_path_100, circuit))
            library_lines = library.readlines()
            nodes_c = 0
            length = 0
            print(critical_nodes)
            critical_nodes = ['N22', 'N23', 'N16', 'net_0_NAND2_6', 'N10', 'N19']
            for index, line in enumerate(library_lines):
                if index in [0, 1, 2, 3]:
                    continue
                if line.startswith('run'):
                    continue
                nodes = line.strip().split('|')[1].replace("'", "").replace('[', "").replace(']', "").strip().split(
                    ', ')
                for cn in critical_nodes[0:6]:
                    if cn in nodes:
                        nodes.remove(cn)
                nodes_c += len(nodes)
                length += 1
            self.nodes_average = nodes_c / length
            print(str(round(self.nodes_average, 2)).replace('.', ','))


if __name__ == '__main__':
    results = GenerateResults("c17")
    # results.critical_nodes_average()
    # results.nodes_above_average()
    results.get_logic_gate_critical_nodes()
    # results.critical_vectors_average()
    # results.get_runtime()
    # print(results.critical_nodes)
    # print(results.vectors_average)
    # print(results.nodes_average)
