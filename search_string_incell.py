import numpy as np
import pandas as pd

# open excel file
discount = pd.read_excel("C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\data\\report\\ส่วนลดไม่รวมค่าธรรมเนียมธนาคาร และขายสด บริการ my ปี2565.xlsx", sheet_name="ALL0865")

# search string in cell "Discount Total"
row, col = np.where(discount == "ขายเงินสดทั้งสิ้น")
print(row, col)

# get value from cell
cash = discount.iloc[row,col+2].values[0] 
print(cash)

entries = np.array(discount)
# print(entries)

df = pd.Series(entries[0]).str.contains("ขายเงินสด")
# print(df)

