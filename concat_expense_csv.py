# https://phyblas.hinaboshi.com/20200304
# รวมไฟล์ csv ให้เป็นไฟล์เดียว

import glob
import os
from datetime import datetime
from subprocess import call
import pandas as pd

path = "D:\\share\\จบ\\จบง.ปี2565\\Expense NT2\\"
output_file = "expense_nt2_2022.csv"
output_path = "D:\\share\\จบ\\จบง.ปี2565\\Expense\\"

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
    datafile = pd.read_csv(file, \
        converters={"YEAR":str, "MONTH":str, "GL_CODE":str, "COST_CENTER":str})

    datafile.columns = datafile.columns.str.replace(" ", "")
    datafile = datafile.dropna(subset=["EXPENSE_VALUE"])
    datafile[value_field] = datafile[value_field].replace(",", "", regex=True)
    datafile[value_field] = datafile[value_field].replace("\(", "-", regex=True)
    datafile[value_field] = datafile[value_field].replace("\)", "", regex=True)
    # datafile[value_field] = datafile[value_field].replace("-", "", regex=True)
    datafile[value_field] = datafile[value_field].replace(" ", "", regex=True)
    
    datafile = datafile[["YEAR", "MONTH", "GL_CODE", "COST_CENTER", "EXPENSE_VALUE"]]
    
    df = pd.concat([df, datafile])

print(df.head)

df.to_csv(output_path + output_file, index=False, float_format="%.2f")


print("end =", datetime.now())