# importing pandas
import pandas as pd

# merging two csv files
df = pd.concat (
    map(pd.read_csv, ['C:\DW\TRN_EXPENSE_BEFORE_20220630.csv', 'C:\DW\TRN_EXPENSE_BEFORE_20220731.csv']),
                ignore_index=True)

print(df.head)

df.to_csv('C:\DW\TRN_EXPENSE_BEFORE_NT1_2022.csv', index=False) # เขียนผลลัพธ์ ลงไฟล์ 

