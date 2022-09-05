# https://pythonbasics.org/read-excel/

import pandas as pd

df = pd.read_excel("read_excel_example.xlsx")
print(df)
print()
df_sheet_name = pd.read_excel("read_excel_example.xlsx", sheet_name="Sheet2")

print(df_sheet_name)
print()
print(df_sheet_name["AA"])
print()
print(df_sheet_name["AA"][1])
print()

for row in df_sheet_name["AA"]:
        print(row)