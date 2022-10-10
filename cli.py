import click
from hecate_commands import Hecate
from hecate.nangate_parser import verilog_to_spice

# Command Group
@click.group(name='hecate_command')
def hecate_command():
    """Tool related commands"""
    pass


@hecate_command.command(name='sensitive_nodes_for_all_input_vectors')
@click.option("-n", "--name", type=str, required=True, help="Your name")
def sensitive_nodes_for_all_input_vectors(name):
    hecate = Hecate(name)
    hecate.sensitive_nodes_for_all_input_values()


@hecate_command.command(name='number_of_vectors_by_sensitive_node')
@click.option("-n", "--name", type=str, required=True, help="Circuit name")
def number_of_vectors_by_sensitive_node(name):
    hecate = Hecate(name)
    hecate.sensitive_nodes_for_all_input_values()
    hecate.critical_nodes()


@hecate_command.command(name='sensitive_nodes_for_a_vector')
@click.option("-n", "--name", type=str, required=True, help="Circuit name")
@click.option("-v", "--vector", type=str, required=True, help="Input vector")
def sensitive_nodes_for_a_vector(name, vector):
    hecate = Hecate(name)
    hecate.sensitive_nodes_for_a_vector(vector)


if __name__ == '__main__':
    hecate_command.add_command(verilog_to_spice)
    hecate_command()