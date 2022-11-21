# https://pythonbasics.org/read-excel/
import glob
import os
from datetime import datetime
import pandas as pd

path = "D:\\share\\ตบ\\TRN_EXPENSE_2022\\"
output_path = "D:\\share\\ตบ\\TRN_EXPENSE_2022\\"
output_file = "10-2022_Data_TRN_EXPENSE.csv"
value_field = "EXPENSE_VALUE"

print("start =", datetime.now())

joined_files = os.path.join(path, "10-2022_Data_TRN_EXPENSE_Part*.csv")
print(joined_files)
joined_list = glob.glob(joined_files)
print(joined_list)

df = pd.DataFrame()

for file in joined_list:
    print(file)

    # datafile = pd.read_csv(file, encoding="cp874")
    # datafile = pd.read_csv(file, encoding="tis-620")
    datafile = pd.read_csv(file, encoding="tis-620", \
                           converters={"YEAR":str, "MONTH":str, "GL_CODE":str, "COST_CENTER":str})

    datafile.columns = datafile.columns.str.replace(" ", "")
    datafile = datafile.dropna(subset=["EXPENSE_VALUE"])
    datafile[value_field] = datafile[value_field].replace(",", "", regex=True)
    datafile[value_field] = datafile[value_field].replace("\(", "-", regex=True)
    datafile[value_field] = datafile[value_field].replace("\)", "", regex=True)
    # datafile[value_field] = datafile[value_field].replace("-", "", regex=True)
    datafile[value_field] = datafile[value_field].replace(" ", "", regex=True)
    
    # datafile = datafile[["YEAR", "MONTH", "GL_CODE", "COST_CENTER", "EXPENSE_VALUE"]]
    
    df = pd.concat([df, datafile])

print(df.head)

df.to_csv(output_path + output_file, index=False, float_format="%.2f")

# df = pd.read_csv("D:\\share\\ตบ\\TRN_EXPENSE_2022\\10-2022_Data_TRN_EXPENSE_Part1.csv", encoding="tis-620")

# print("Grand Total = ", "{:,.2f}".format(df['EXPENSE_VALUE'].sum()))
print("end =", datetime.now())