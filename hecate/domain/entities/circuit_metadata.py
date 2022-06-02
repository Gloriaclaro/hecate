from enum import Enum


class SupplyIndex(Enum):
    SUPPLY_KEY = 0
    SUPPLY_NAME = 1


class Supply:
    def __init__(self, supply: list):
        self.__supply: list = supply

    def get_supply_name(self):
        return self.__supply[SupplyIndex.SUPPLY_NAME.value]

    def get_supply_key(self):
        return self.__supply[SupplyIndex.SUPPLY_KEY.value]


class GroundIndex(Enum):
    GROUND_KEY = 0
    GROUND_NAME = 1


class Ground:
    def __init__(self, ground: list):
        self.__ground: list = ground

    def get_ground_name(self):
        return self.__ground[GroundIndex.GROUND_NAME.value]

    def get_ground_key(self):
        return self.__ground[GroundIndex.GROUND_KEY.value]


class NodeTypeIndex(Enum):
    NODE_TYPE_KEY = 0
    NODE_TYPE = 1


class InputIndex(Enum):
    NODE_TYPE_KEY = 0
    NODE_TYPE = 1


class OutputIndex(Enum):
    NODE_TYPE_KEY = 0
    NODE_TYPE = 1


class NodeType:
    def __init__(self, node_type: list):
        self.__node_type: list = node_type

    def get_node_type(self):
        return self.__node_type[NodeTypeIndex.NODE_TYPE.value]

    def get_node_type_key(self):
        return self.__node_type[NodeTypeIndex.NODE_TYPE_KEY.value]


class Input:
    def __init__(self, inputs: list):
        self.__input: list = inputs

    def get_inputs(self):
        return self.__input[InputIndex.NODE_TYPE.value:]

    def get_input_key(self):
        return self.__input[InputIndex.NODE_TYPE_KEY.value]


class Output:
    def __init__(self, output: list):
        self.__node_type: list = output

    def get_output(self):
        return self.__node_type[OutputIndex.NODE_TYPE.value]

    def get_output_key(self):
        return self.__node_type[OutputIndex.NODE_TYPE_KEY.value]


class CircuitMetadata:

    def __init__(self, supply: Supply, ground: Ground, n_type: NodeType, p_type: NodeType,
                 inputs: Input, output: Output):
        self.__supply: Supply = supply
        self.__ground: Ground = ground
        self.__n_type: NodeType = n_type
        self.__p_type: NodeType = p_type
        self.__inputs = inputs
        self.__output = output

    def get_p_type(self):
        return self.__p_type.get_node_type()

    def get_n_type(self):
        return self.__n_type.get_node_type()

    def get_supply(self):
        return self.__supply.get_supply_name()

    def get_ground(self):
        return self.__ground.get_ground_name()

    def get_output(self):
        return self.__output.get_output()

    def get_inputs(self):
        return self.__inputs.get_inputs()
