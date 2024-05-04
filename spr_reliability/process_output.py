import pandas as pd

for circuit in ['c432', 'c499', 'c880', 'c1355', 'c1908',  'c3540']:
    # , 'c5315', 'c6288', 'c7552']:

    df = pd.read_csv(f'spr_output/{circuit}_spr_output.txt')
    new_df = df.pivot(index='percentage', columns='method', values='spr_reliability')
    new_df.to_csv(f'spr_output/{circuit}_spr_output_pivot.txt')