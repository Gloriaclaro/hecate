gates = []
# with open('hecate/circuits/library/NangateLibrary.spi', 'r') as lib:
#     lines = lib.readlines()
#     for line in lines:
#
#         if line.startswith('.SUBCKT'):
#             gates.append(line.split(' ')[1])
for circuit in ['C17_nangate', 'c432', 'c499', 'c880', 'c1355', 'c1908', 'c3540', 'c5315', 'c6288', 'c7552']:
    with open(f'hecate/circuits/verilog/{circuit}.v', 'r') as c:
        lines = c.readlines()
        is_logic_gate = False
        for line in lines:
            line = line.strip()
            if line == '\n' or line == 'endmodule':
                continue
            if line.startswith('wire'):
                is_logic_gate = True
                continue
            if is_logic_gate:
                if line.startswith('n'):
                    continue
                split_line = line.split(' ')
                print(split_line)
                gates.append(split_line[0])
print(len(gates))
gates = sorted(set(gates))
with open('gates.csv', 'w') as agates:
    for gate in gates:
        agates.write(gate + '\n')
