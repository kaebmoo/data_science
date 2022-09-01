## แปลงรหัส GL ค่าใช้จ่าย NT1 ไปเป็น NT ด้วยการทำแบบ vlookup หรือ LEFT JOIN

import pandas as pd # นำเข้า library pandas

# data = pd.read_excel('C:\DW\TRN_EXPESNE_BEFORE_EXCEL_2022.xlsx') # อ่านไฟล์ ไปไว้ตัวแปร data
data = pd.read_csv('C:\\DW\\TRN_EXPENSE_BEFORE_NT1_2022.csv')
lookup = pd.read_csv('C:\\DW\\EXPENSE_GL_CODE_NT1_NT.csv', encoding= 'tis-620') # อ่านไฟล์ ไปไว้ใน lookup
org = pd.read_csv('D:\share\master\MASTER_ORGANIZATION_NT.csv', sep='\t')

# print(df.to_string()) 
# print(df)

print(data.head()) # พิมพ์ โครงสร้างไฟล์ data ออกมาดู
print(lookup.head())
print(org.head())

# dg['GL_CODE_NT1'] = dg['GL_CODE_NT1'].astype(int)
data['GL_CODE'] = data['GL_CODE'].astype(str) # เปลี่ยน column GL_CODE ให้เป็น string
data.rename(columns={'GL_CODE': 'GL_CODE_NT1'}, inplace=True) # เปลี่ยนชื่อ column GL_CODE เป็น GL_CODE_NT1

# ทำการ merge หรือ การทำแบบ vlookup ของ excel / left join
mod = pd.merge(
    data,
    lookup,
    left_on = ['GL_CODE_NT1'],
    right_on = ['GL_CODE_NT1'],
    how = 'left'
    )

print(mod.head())

del mod['GL_CODE_NT1'] # ลบ column GL_CODE_NT1
del mod['GL_NAME_NT1']

print(mod.head())

output = pd.merge(mod, org, left_on=['COST_CENTER'], right_on=['COST_CENTER'], how='left')


output.to_csv('C:\\DW\\EXPENSE_DATA_2022.csv', index=False) # เขียนผลลัพธ์ ลงไฟล์ 
# mod.to_csv('C:\\DW\\EXPENSE_DATA_2022.csv', index=False) # เขียนผลลัพธ์ ลงไฟล์ 

# help me
# https://note.nkmk.me/en/python-pandas-dataframe-rename/#:~:text=You%20can%20use%20the%20rename,change%20column%2Findex%20name%20individually.&text=Specify%20the%20original%20name%20and,is%20for%20the%20index%20name.
# https://www.statology.org/you-are-trying-to-merge-on-object-and-int64-columns/
# https://betterprogramming.pub/vlookups-are-cancelled-why-python-pandas-are-a-much-better-way-to-merge-data-dbce0126166a
# https://datagy.io/vlookup-in-python-and-pandas-using-map-or-merge/
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
# https://www.educative.io/answers/how-to-delete-a-column-in-pandas
