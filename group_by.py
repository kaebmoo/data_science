## เปิดไฟล์ แสดงโครงสร้างของ csv
# จัดกลุ่ม เพื่อหาผลรวม
# หาผลรวมตามเงื่อนไขที่ระบุ

# https://stackoverflow.com/questions/20937538/how-to-display-pandas-dataframe-of-floats-using-a-format-string-for-columns
# https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
# https://stackoverflow.com/questions/28236305/how-do-i-sum-values-in-a-column-that-match-a-given-condition-using-pandas
# https://datatofish.com/left-right-mid-pandas/

import pandas as pd # นำเข้า library pandas

pd.options.display.float_format = '{:,.2f}'.format

data = pd.read_csv('C:\\Users\\CAT\\Documents\\GitHub\\nt\\EXPENSE_REPORT_2021-2022.csv') # อ่านไฟล์ ไปไว้ตัวแปร data

print(data.head()) # พิมพ์ โครงสร้างไฟล์ data ออกมาดู
print(data.info())

## print("Grand Total = ", end=" ")
grand_total = data['AMOUNT'].sum()
print(grand_total)
print("Grand Total = ", "{:,.2f}".format(data['AMOUNT'].sum()))


grand_total_2022 = data.loc[data['YEAR'] == 2022, 'EXPENSE_VALUE'].sum()
print("Grand Total = ", "{:,.2f}".format(grand_total_2022))


grand_total_2022 = data.loc[data['DATE'].str[-4:] == '2022', 'EXPENSE_VALUE'].sum()
print("Grand Total = ", "{:,.2f}".format(grand_total_2022))

months = [1,2,3,4,5,6,7,8,9,10,11,12]
for month in months:
    grand_total_month = data.loc[data['MONTH'] == month, 'EXPENSE_VALUE'].sum()
    print("Total "+str(month)+" = ", "{:,.2f}".format(grand_total_month))
    
print(data.groupby('MONTH')['EXPENSE_VALUE'].sum())
