## เปิดไฟล์ แสดงโครงสร้างของ csv 

import pandas as pd # นำเข้า library pandas

data = pd.read_csv('C:\DW\TRN_EXPENSE_BEFORE_20220731.csv') # อ่านไฟล์ ไปไว้ตัวแปร data
lookup = pd.read_csv('C:\DW\EXPENSE_GL_CODE_NT1_NT.csv', encoding= 'tis-620') # อ่านไฟล์ ไปไว้ใน lookup

# print(df.to_string()) 
# print(df)

print(data.head()) # พิมพ์ โครงสร้างไฟล์ data ออกมาดู
print(lookup.head())

print("Grand Total = ", end=" ")
print(data['EXPENSE_VALUE'].sum())

print("Grand Total = ", "{:,.2f}".format(data['EXPENSE_VALUE'].sum()))