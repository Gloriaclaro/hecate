import json
import re


def create_protected_verilog(circuit_name: str):
    gates_by_percentage = {}
    with open(f'outputs/max_sum_vs_deep_fanout/{circuit_name}.csv', 'r') as selected_gates:
        buffer = ""
        lines = selected_gates.readlines()
        for line in lines[1:]:
            buffer += line
            percentage = buffer.split(',')[1]
            columns = re.split('"', buffer)
            if len(columns) != 7:
                continue
            # if len(columns) != 14:
            #     continue
            buffer = ""
            column3 = columns[1].replace("'", '"').replace('\n', '')[1:-1]
            column4 = columns[3].replace("'", '"').replace('\n', '')[1:-1]
            column5 = columns[5].replace("'", '"').replace('\n', '')[1:-1]
            # if columns[1] == '1.0':
            #     print(columns[1], len(json.loads(column3)))
            gates_by_percentage.update({
                percentage: {
                    "gates_max": json.loads("["+column3+"]"),
                    "gates_sum": json.loads("["+column4+"]"),
                    "gates_deep_fanout": json.loads("["+column5+"]")
                }})

    for percentage in gates_by_percentage.keys():
        for method in gates_by_percentage[percentage].keys():
            with open(f'hecate/circuits/verilog/{circuit_name}.v', 'r') as cir:
                lines = cir.readlines()
                with open(f'spr_reliability/spr_verilog_input/{circuit_name}/{circuit_name}_protected_{method}_{percentage}.v', 'w') as cir_p:
                    is_logic_gate = False
                    for line in lines:
                        line_strip = line.strip()
                        if not is_logic_gate or line == '\n' or line == 'endmodule\n':
                            cir_p.write(line)
                            if not line_strip.startswith('wire'):
                                continue
                            is_logic_gate = True
                        split_line = line.split(' ')
                        split_line = [i for i in split_line if i]
                        if split_line[1].split('(')[0] in gates_by_percentage[percentage][method]:
                            split_line[0] = split_line[0] + '_p'
                            new_line = ' '.join(split_line)

                            cir_p.write(new_line)
                        else:
                            cir_p.write(line)


def create_protected_verilog_c17(circuit_name: str):
    gates_by_percentage = {}
    with open(f'outputs/max_sum_vs_deep_fanout/{circuit_name}.csv', 'r') as selected_gates:
        buffer = ""
        lines = selected_gates.readlines()
        for line in lines[1:]:
            buffer += line

            columns = buffer.split(',')

            if len(columns) != 14:
                continue
            buffer = ""
            column3 = columns[3].replace("'", '"').replace(' ', ',').replace('\n', '')
            column4 = columns[4].replace("'", '"').replace(' ', ',').replace('\n', '')
            column5 = columns[5].replace("'", '"').replace(' ', ',').replace('\n', '')
            print(column3)
            gates_by_percentage.update({
                columns[1]: {
                    "gates_max": json.loads(column3),
                    "gates_sum": json.loads(column4),
                    "gates_deep_fanout": json.loads(column5)
                }})
    print(gates_by_percentage)
    for percentage in gates_by_percentage.keys():
        print(percentage)
        for method in gates_by_percentage[percentage].keys():
            with open(f'hecate/circuits/verilog/C17_nangate.v', 'r') as cir:
                lines = cir.readlines()

                with open(f'outputs/spr_verilog_input/{circuit_name}/{circuit_name}_protected_{method}_{percentage}.v', 'w') as cir_p:
                    is_logic_gate = False
                    for line in lines:
                        line_strip = line.strip()
                        if not is_logic_gate or line == '\n' or line == 'endmodule':
                            cir_p.write(line)
                            if not line_strip.startswith('wire'):
                                continue
                            is_logic_gate = True
                        split_line = line.split(' ')
                        print(split_line)
                        # split_line = [i for i in split_line if i]
                        if split_line[1] in gates_by_percentage[percentage][method]:
                            split_line[0] = split_line[0] + '_p'
                            new_line = ' '.join(split_line)
                            cir_p.write(new_line)
                        elif not line_strip.startswith('wire'):
                            cir_p.write(line)

def create_protected_verilog_ctrl(circuit_name: str):
    gates_by_percentage = {}
    with open(f'outputs/max_sum_vs_deep_fanout/{circuit_name}.csv', 'r') as selected_gates:
        buffer = ""
        lines = selected_gates.readlines()
        for line in lines[1:]:
            buffer += line
            percentage = line.split(',')[1]
            columns = re.split('"', buffer)
            if percentage == '0.0':
                gates_by_percentage.update({
                    percentage: {
                        "gates_max": [],
                        "gates_sum": [],
                        "gates_deep_fanout": []
                    }})
            if len(columns) != 7:
                continue

            # if len(columns) != 14:
            #     continue
            buffer = ""
            column3 = columns[1].replace("'", '"').replace('\n', '')[1:-1]
            column4 = columns[3].replace("'", '"').replace('\n', '')[1:-1]
            column5 = columns[5].replace("'", '"').replace('\n', '')[1:-1]
            gates_by_percentage.update({
                percentage: {
                    "gates_max": json.loads("["+column3+"]"),
                    "gates_sum": json.loads("["+column4+"]"),
                    "gates_deep_fanout": json.loads("["+column5+"]")
                }})

    print(gates_by_percentage.keys())
    for percentage in gates_by_percentage.keys():
        for method in gates_by_percentage[percentage].keys():
            with open(f'hecate/circuits/verilog/{circuit_name}.v', 'r') as cir:
                lines = cir.readlines()
                with open(f'spr_reliability/spr_verilog_input/{circuit_name}/{circuit_name}_protected_{method}_{percentage}.v', 'w') as cir_p:
                    is_logic_gate = False
                    buffer = ""
                    for line in lines:
                        buffer += line
                        if ";" not in buffer:
                            continue
                        line = buffer
                        buffer = ""
                        line_strip = line.strip()

                        if not is_logic_gate or line == '\n' or line == 'endmodule\n':
                            cir_p.write(line)
                            if not line_strip.startswith('wire'):
                                continue
                            is_logic_gate = True

                        split_line = line.split(' ')
                        split_line = [i for i in split_line if i]
                        if split_line[1].split('(')[0] in gates_by_percentage[percentage][method]:
                            split_line[0] = split_line[0] + '_p'
                            new_line = ' '.join(split_line)

                            cir_p.write(new_line)
                        else:
                            cir_p.write(line)

if __name__ == '__main__':
    for circuit in ['int2float', 'cavlc', 'router', 'i2c', 'priority',  'dec', 'ctrl', 'arbiter']:

        print(circuit)
        create_protected_verilog_ctrl(circuit)
# for circuit in ['c432', 'c499', 'c880', 'c1355', 'c1908', 'c3540', 'c5315', 'c6288', 'c7552']:

# create_protected_verilog_c17('c17')