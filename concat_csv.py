# https://phyblas.hinaboshi.com/20200304
# รวมไฟล์ csv ให้เป็นไฟล์เดียว

import glob
import os
from datetime import datetime
from subprocess import call
import pandas as pd

path = "D:\\share\\จบ\\จบง.ปี2565\\Expense NT1\\"
output_path = "D:\\share\\จบ\\จบง.ปี2565\\Expense NT1\\"
output_file = "expense_nt1_2022.csv_output"
value_field = "EXPENSE_VALUE"
# path = "D:\\DW\\ลูกหนี้คงเหลือ\\"

print("start =", datetime.now())

joined_files = os.path.join(path, "*.csv")
print(joined_files)
joined_list = glob.glob(joined_files)
print(joined_list)

df = pd.DataFrame()

for file in joined_list:
    print(file)

    # datafile = pd.read_csv(file, encoding="cp874")
    # datafile = pd.read_csv(file, encoding="tis-620")
    datafile = pd.read_csv(file)

    datafile.columns = datafile.columns.str.replace(" ", "")
    datafile[value_field] = datafile[value_field].replace(",", "", regex=True)
    datafile[value_field] = datafile[value_field].replace("\(", "-", regex=True)
    datafile[value_field] = datafile[value_field].replace("\)", "", regex=True)
    # datafile[value_field] = datafile[value_field].replace("-", "", regex=True)
    datafile[value_field] = datafile[value_field].replace(" ", "", regex=True)
    
    
    df = pd.concat([df, datafile])

print(df.head)

df.to_csv(output_path + output_file, index=False)


print("end =", datetime.now())