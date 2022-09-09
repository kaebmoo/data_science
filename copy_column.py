# copy column

import pandas as pd # นำเข้า library pandas


data = pd.read_csv('C:\\Users\\CAT\\Documents\\GitHub\\nt\\EXPENSE_REPORT_2021-2022.csv') # อ่านไฟล์ ไปไว้ตัวแปร data

data['EXPENSE_VALUE'] = data['AMOUNT']

data.to_csv('C:\\Users\\CAT\\Documents\\GitHub\\nt\\EXPENSE_REPORT_2021-2022.csv', index=False) # เขียนผลลัพธ์ ลงไฟล์ 