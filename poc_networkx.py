import networkx as nx
from typing import Union

inputs = ["a", "b", "c"]
# Node is a signal
# signal type root: inputs, output, supply or ground
# signal p: p-type
# signal n: n-type
circuit = nx.DiGraph()
circuit.add_nodes_from([
    ("root_vdd", {"signal": 1}),
    ("root_x1", {"signal": "x"}),
    ("root_x2", {"signal": "x"}),
    ("p_a", {"signal": "x"}),
    ("p_c", {"signal": "x"}),
    ("p_b", {"signal": "x"}),
    ("n_a", {"signal": "x"}),
    ("n_c", {"signal": "x"}),
    ("n_b", {"signal": "x"}),
    ("root_out", {"signal": "x"}),
    ("root_gnd", {"signal": 0}),
])

# PULL UP
circuit.add_edges_from([("root_vdd", "p_a", {"signal": "x"}),
                        ("p_a", "root_x1", {"signal": "x"}),
                        ("root_x1", "p_c", {"signal": "x"}),
                        ("root_x1", "p_b", {"signal": "x"}),
                        ("p_b", "root_out", {"signal": "x"}),
                        ("p_c", "root_out", {"signal": "x"})
                       ])


# input a = 0; b = 0; c = 0
a = 1
b = 0
c = 1
circuit.nodes["p_a"]["signal"] = a
circuit.nodes["p_b"]["signal"] = b
circuit.nodes["p_c"]["signal"] = c
circuit.nodes["n_a"]["signal"] = a
circuit.nodes["n_b"]["signal"] = b
circuit.nodes["n_c"]["signal"] = c


def get_next_node(key: str, circuit):
    adj_node = circuit.adj[key]
    return list(adj_node._atlas)


def set_edge_signal_pmos(next_node: str, node: str, circuit):
    last_node_signal = circuit.nodes[node]["signal"]
    if circuit.nodes[next_node]["signal"] == 0:
        circuit[node][next_node]["signal"] = last_node_signal
    else:
        circuit[node][next_node]["signal"] = last_node_signal
        last_node_signal = 'x'
    return last_node_signal


def set_edge_signal_root(last_node_signal: Union[str, int], node: str, next_node: str, circuit):
    if circuit.nodes[next_node]["signal"] == 'x':
        circuit.nodes[next_node]["signal"] = last_node_signal
    circuit[node][next_node]["signal"] = last_node_signal



next_nodes = ["root_vdd"]
last_node_signal = 1
while next_nodes:
    for node in next_nodes:
        next_nodes = get_next_node(node, circuit)
        for next_node in next_nodes:
            if "root" in next_node:
                set_edge_signal_root(last_node_signal, node, next_node, circuit)
                continue
            last_node_signal = set_edge_signal_pmos(next_node, node, circuit)



# PULL DOWN
circuit.add_edges_from([("root_gnd", "n_a", {"signal": "x"}),
                        ("root_gnd", "n_b", {"signal": "x"}),
                        ("n_b", "root_x2", {"signal": "x"}),
                        ("root_x2", "n_c", {"signal": "x"}),
                        ("n_c", "root_out", {"signal": "x"}),
                        ("n_a", "root_out", {"signal": "x"})
                       ])


def set_edge_signal_nmos(next_node: str, node: str, circuit):
    last_node_signal = circuit.nodes[node]["signal"]
    if circuit.nodes[next_node]["signal"] == 1:
        circuit[node][next_node]["signal"] = last_node_signal
    else:
        circuit[node][next_node]["signal"] = last_node_signal
        last_node_signal = 'x'
    return last_node_signal

next_nodes = ["root_gnd"]
last_node_signal = 0
last_node_signal_by_node = {}
while next_nodes:
    for node in next_nodes:
        next_nodes = get_next_node(node, circuit)
        if node not in list(last_node_signal_by_node.keys()):
            last_node_signal_by_node[node] = last_node_signal
        for next_node in next_nodes:
            if "root" in next_node:
                set_edge_signal_root(last_node_signal_by_node[node], node, next_node, circuit)
                continue
            last_node_signal = set_edge_signal_nmos(next_node, node, circuit)
            last_node_signal_by_node[next_node] = last_node_signal


def get_predecessors(key: str, circuit):
    adj_node = circuit.predecessors(key)
    return list(adj_node)


def set_signal_out(last_signal, node, next_node, circuit):
    if circuit[next_node][node]["signal"] == 'x':
        circuit[next_node][node]['signal'] = last_signal
    if next_node.startswith('root') and circuit.nodes[next_node]['signal'] == 'x':
        circuit.nodes[next_node]['signal'] = last_signal
    return last_signal

next_nodes = ["root_out"]
last_node_signal = circuit.nodes["root_out"]["signal"]
last_node_signal_by_node = {}
while next_nodes:
    for node in next_nodes:
        next_nodes = get_predecessors(node, circuit)
        if node not in list(last_node_signal_by_node.keys()):
            last_node_signal_by_node[node] = last_node_signal
        for next_node in next_nodes:
            if node.startswith('n') and circuit.nodes[node]["signal"] == 0:
                break
            elif node.startswith('p') and circuit.nodes[node]["signal"] == 1:
                break
            else:
                last_node_signal = set_signal_out(last_node_signal_by_node[node], node, next_node, circuit)
                last_node_signal_by_node[next_node] = last_node_signal

# IDENTIFY SENSITIVE NODES
possible_sensitive_nodes = ["root_x1", "root_x2"]

# NODES N-TYPE
circuit.nodes["root_x2"]["type"] = "n"

# NODES P-TYPE
circuit.nodes["root_x1"]["type"] = "p"

sensitive_nodes_list = ["root_out"]

for node in possible_sensitive_nodes:
    if circuit.nodes[node]["signal"] == 0 and circuit.nodes[node]['type'] == 'p':
        sensitive_nodes_list.append(node)
    elif circuit.nodes[node]["signal"] == 1 and circuit.nodes[node]['type'] == 'n':
        sensitive_nodes_list.append(node)
    else:
        continue
#
print(f"{a}{b}{c}", sensitive_nodes_list)
#
# NODES SIGNAL
print(circuit.nodes.data())
#
# EDGES SIGNAL
for n, nbrs in circuit.adj.items():
    print(n, nbrs)