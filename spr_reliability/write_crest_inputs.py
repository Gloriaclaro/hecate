import os, glob
import subprocess


for circuit in ['c432', 'c499', 'c880', 'c1355', 'c1908', 'c2670', 'c3540', 'c5315', 'c6288', 'c7552']:
    path = f'spr_verilog_input/{circuit}'
    with open(f'spr_output/{circuit}_spr_output.txt', 'w') as spr_out:
        spr_out.writelines("circuit,percentage,method,spr_reliability\n")
        for filename in glob.glob(os.path.join(path, '*.v')):
            file = filename.split('\\')[1]
            file_info = file.split('_')
            percentage = file_info[-1][:-2]
            method = file_info[2] + "_" + file_info[3]
            prompt_input = f"java -jar Crest-D.jar spr_verilog_input/{circuit}/{file} nangate.genlib probabilisticTransferMatrix.txt\n"
            print(prompt_input)
            proc = subprocess.Popen(prompt_input, shell=True, stdin=subprocess.PIPE, stdout = subprocess.PIPE)
            out, err = proc.communicate()
            spr_reliability = out.decode("utf-8")
            spr_out.writelines(f"{circuit},{percentage},{method},{spr_reliability.strip()}\n")
