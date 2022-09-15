# ใช้เปรียบเทียบข้อมูลระหว่าง 2 ไฟล์ว่า มีความแตกต่างตรงไหน
# เช่น เมื่อมีการปรับปรุงบัญชี แล้วต้องการทราบว่ามีการปรับรายการอะไรบ้าง
# *** มีการรวม GL_CODE และ COST_CENTER ที่เหมือนกันแล้วหาผลรวม *** group by
# ทั้งสองไฟล์ต้องมี column เหมือนกัน
# แสดงผลต่างทางหน้าจอ และเขียนลงไฟล์ 

import pandas as pd
from datetime import datetime

print("start =", datetime.now())

# file เดิม ที่จะใช้เปรียบเทียบ
old_file = "C:\\DW\\tmp\\3.Expense NT1_20220331.xlsx"
# file ใหม่
new_file = "C:\\DW\\tmp\\3.Expense NT1_20220331a.xlsx"
# df2 = pd.read_excel("D:\\share\\จบ\\จบง.ปี2565\\Expense NT1\\3.Expense NT1_20220331.xlsx")
# output file ผลการเปรียบเทียบ
output_file = "C:\\DW\\tmp\\diff.csv"

print("Reading...")
df1 = pd.read_excel(old_file) 
df2 = pd.read_excel(new_file)


print("Processing...")
# ใช้อันใดอันหนึ่งก็ได้ 
output_old = df1.merge(df2,indicator = True, how='left').loc[lambda x : x['_merge']!='both']
output_new = df1.merge(df2,indicator = True, how='right').loc[lambda x : x['_merge']!='both']
# output = df1[~df1.apply(tuple,1).isin(df2.apply(tuple,1))]


output_old.rename(columns={'EXPENSE_VALUE': 'EXPENSE_VALUE_OLD'}, inplace=True)
output_new.rename(columns={'EXPENSE_VALUE': 'EXPENSE_VALUE_NEW'}, inplace=True)

print(output_old)
print(output_new)

merged = pd.concat([output_old, output_new])

output = merged.groupby(["GL_CODE", "COST_CENTER"]).agg({'EXPENSE_VALUE_OLD': ['sum'], 'EXPENSE_VALUE_NEW': ['sum'] })
print(output)
output.to_csv(output_file, index=True)

print("end =", datetime.now())

# https://stackoverflow.com/questions/48647534/python-pandas-find-difference-between-two-data-frames
# https://jamesrledoux.com/code/group-by-aggregate-pandas

# For columns, try this:
#set(df1.columns).symmetric_difference(df2.columns)