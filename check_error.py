import pandas as pd
from datetime import datetime

print("start =", datetime.now())

data = pd.read_csv('D:\share\ตบ\TRN_EXPENSE_2022\CO_202207_OUTPUT_ERRORS.csv')

bool_series = pd.isnull(data['ประเภทต้นทุน'])

print(data[bool_series])

print("end =", datetime.now())

## https://www.geeksforgeeks.org/working-with-missing-data-in-pandas