import pandas as pd
from datetime import datetime

print("start =", datetime.now())
# sheet_name='TRN_EXPENSE_202207_Part1'
df1 = pd.read_excel("D:\\share\\ตบ\\TRN_EXPENSE_2022\\072022_Data_TRN_EXPENSE_Part1.xlsx")
df2 = pd.read_excel("D:\\share\\ตบ\\TRN_EXPENSE_2022\\072022_Data_TRN_EXPENSE_Part2.xlsx")
df3 = pd.read_excel("D:\\share\\ตบ\\TRN_EXPENSE_2022\\072022_Data_TRN_EXPENSE_Part3.xlsx")
df4 = pd.read_excel("D:\\share\\ตบ\\TRN_EXPENSE_2022\\072022_Data_TRN_EXPENSE_Part4.xlsx")
df5 = pd.read_excel("D:\\share\\ตบ\\TRN_EXPENSE_2022\\072022_Data_TRN_EXPENSE_Part5.xlsx")

df = pd.concat([df1,df2,df3,df4,df5], axis=0, join='outer')
df.to_csv("D:\\share\\ตบ\\TRN_EXPENSE_2022\\072022_Data_TRN_EXPENSE.csv", index=False)

print("end =", datetime.now())
print(df1.head)
