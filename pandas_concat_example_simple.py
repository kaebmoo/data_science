# https://gist.github.com/ryansmccoy/c4812a204bfae7c3281179a7fcf68d1b
import glob
toglob = r'B:\TOMERGE'
files = glob.glob(toglob+'\*')

import pandas as pd
frame = pd.DataFrame()
list_ = []

for file_ in files:
    df = pd.read_csv(file_,index_col=None, header=0,encoding='utf-8', low_memory=False, error_bad_lines=False )
    print('imported csv file: ', file)
    list_.append(df)

frame = pd.concat(list_)

frame.to_csv(toglob+'\combined_csv_file.csv', encoding='utf-8')