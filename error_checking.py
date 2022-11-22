import pandas as pd
from datetime import datetime

input_path = "D:\\share\\ตบ\\TRN_EXPENSE_2022\\"
input_file = "10-2022_Data_TRN_EXPENSE.csv"

output_path = "D:\\share\\ตบ\\TRN_EXPENSE_2022\\"
output_file = "CO_202210_DATA.csv"

print("error checking...")

print("start =", datetime.now())

data = pd.read_csv(output_path + output_file)

bool_series = pd.isnull(data['ประเภทต้นทุน'])
print(data[bool_series])

bool_series = pd.isnull(data['หมวดบัญชี'])
print(data[bool_series])

# BUSINESS_PROCESS_CODE
bool_series = pd.isnull(data['BUSINESS_PROCESS_CODE'])
print(data[bool_series])

print("end =", datetime.now())