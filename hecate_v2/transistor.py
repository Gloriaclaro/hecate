
class Transistor:
    def __init__(self, name: str, source, gate, drain, bulk, transistor_type: str):
        self.name = name
        self.source = source
        self.gate = gate
        self.drain = drain
        self.bulk = bulk
        self.transistor_type = transistor_type

    def get_transistor_name(self):
        return self.name

    def get_source(self):
        return self.source

    def get_gate(self):
        return self.gate

    def get_drain(self):
        return self.drain

    def get_bulk(self):
        return self.bulk

    def get_type(self):
        return self.transistor_type



