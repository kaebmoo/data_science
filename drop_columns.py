import pandas as pd
from datetime import datetime

input_path = "D:\\share\\ตบ\\TRN_EXPENSE_2022\\"
input_file = "10-2022_Data_TRN_EXPENSE.csv"

output_path = "D:\\share\\ตบ\\TRN_EXPENSE_2022\\"
output_file = "CO_202210_DATA.csv"

print("start =", datetime.now())
data = pd.read_csv(input_path + input_file)
data = data[["YEAR","MONTH","PRODUCT_KEY","BUSINESS_PROCESS_CODE","GL_CODE","FIX_VAR_EXPENSE_FLAG","DIRECT_INDIRECT_EXPENSE_FLAG","EXPENSE_VALUE"]]
data.to_csv(output_path + output_file, index=False)
print("end =", datetime.now())
