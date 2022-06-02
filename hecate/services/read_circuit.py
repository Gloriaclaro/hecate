from hecate.domain.entities.circuit_metadata import CircuitMetadata, Supply, Ground, NodeType, Input, Output
from hecate.domain.entities.middle_signal import MiddleSignal
from hecate.domain.entities.n_signal import NSignal
from hecate.domain.entities.p_signal import PSignal
from hecate.domain.entities.root_signal import RootSignal
from hecate.domain.entities.transistor import Transistor


class ReadCircuit:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.circuit_metadata: CircuitMetadata = None
        self.p_transistors_list = []
        self.n_transistors_list = []
        self.__signals_list = []
        self.__signals_name_list = []

    def read_ngspice_file(self):
        file = open(self.file_path)
        file_lines = file.readlines()
        metadata_lines = file_lines[:6]
        transistors_list = file_lines[6:]
        self._create_metadata(metadata_lines)
        self._create_root_signals()
        self._create_transistors(transistors_list)

    def get_signals_list(self):
        return self.__signals_list

    def _create_metadata(self, metadata_lines: list):
        supply_list = metadata_lines[0].strip().split(" ")
        supply = Supply(supply=supply_list)

        ground_list = metadata_lines[1].strip().split(" ")
        ground = Ground(ground=ground_list)

        p_type_list = metadata_lines[2].strip().split(" ")
        p_type = NodeType(node_type=p_type_list)

        n_type_list = metadata_lines[3].strip().split(" ")
        n_type = NodeType(node_type=n_type_list)

        inputs_list = metadata_lines[4].strip().split(" ")
        inputs = Input(inputs=inputs_list)

        output_list = metadata_lines[5].strip().split(" ")
        output = Output(output=output_list)

        self.circuit_metadata = CircuitMetadata(
            supply=supply,
            ground=ground,
            n_type=n_type,
            p_type=p_type,
            inputs=inputs,
            output=output
        )

    def _create_transistors(self, transistors: list):
        for raw_transistor in transistors:
            transistor = Transistor(raw_transistor.strip().split(" "))
            transistor_type = transistor.get_type()
            self._create_signal(transistor, transistor_type)
            if transistor_type == self.circuit_metadata.get_n_type():
                self.n_transistors_list.append(transistor)
            elif transistor_type == self.circuit_metadata.get_p_type():
                self.p_transistors_list.append(transistor)

    def _create_root_signals(self):
        supply = self.circuit_metadata.get_supply()
        ground = self.circuit_metadata.get_ground()
        output = self.circuit_metadata.get_output()
        self.__signals_list = [
            (supply, {"signal": RootSignal(supply, 1)}),
            (ground, {"signal": RootSignal(ground, 0)}),
            (output, {"signal": MiddleSignal(output)})
        ]
        self.__signals_name_list = [
            supply, ground, output
        ]

    def _create_signal(self, transistor: Transistor, transistor_type: str):

        drain = transistor.get_drain_name()
        source = transistor.get_source_name()
        gate = transistor.get_gate_name()

        if drain not in self.__signals_name_list:
            self.__signals_list.append((drain, {"signal": MiddleSignal(drain)}))
            self.__signals_name_list.append(drain)

        if source not in self.__signals_name_list:
            self.__signals_list.append((source, {"signal": MiddleSignal(source)}))
            self.__signals_name_list.append(drain)

        if gate not in self.__signals_name_list:
            self.__signals_list.append((f"p_{gate}", {"signal": PSignal(gate)}))
            self.__signals_list.append((f"n_{gate}", {"signal": NSignal(gate)}))
            self.__signals_name_list.append(gate)












