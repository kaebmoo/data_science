## เปิดไฟล์ แสดงโครงสร้างของ csv 

import pandas as pd # นำเข้า library pandas

# https://stackoverflow.com/questions/27896214/reading-tab-delimited-file-with-pandas-works-on-windows-but-not-on-mac
# อ่านไฟล์ ไปไว้ตัวแปร data ข้อมูลกั้นระหว่าง fields ด้วยเครื่องหมาย Tab
data = pd.read_csv('D:\share\master\MASTER_PRODUCT_NT.csv', sep='\t')

# อ่านไฟล์ เข้ารหัสแบบ tis-620; ไว้ใน lookup 
lookup = pd.read_csv('C:\DW\EXPENSE_GL_CODE_NT1_NT.csv', encoding= 'tis-620') 
org = pd.read_csv('D:\share\master\MASTER_ORGANIZATION_NT.csv', sep='\t')

# print(data.to_string()) 
# print(data)

print(data.head()) # พิมพ์ โครงสร้างไฟล์ data ออกมาดู
print(lookup.head())

print(org)