# YEAR,MONTH,PRODUCT_KEY,BUSINESS_PROCESS_CODE,GL_CODE,EXPENSE_VALUE
# 2022,7,181050011,1R00000N0404,8160110101,0.59
# 2022,7,181050011,1R00000N0408,8160110101,6.14
# 2022,7,181050011,1R00000N0419,8160110101,1.25
# 2022,7,181050012,1C00400N0101,8160110101,6.25
# 2022,7,181050012,1C00400N0202,8160110101,46.01

import pandas as pd
from datetime import datetime

input_path = "D:\\share\\ตบ\\TRN_EXPENSE_2022\\"
input_file = "TRN_EXPENSE_NT1_20221031.csv"

master_path = "D:\\share\\master\\"
cost_type_co_master = "MASTER_CO_COST_TYPE.csv"
accounting_category_co_master = "MASTER_CO_ACCOUNTING_CATEGORY.csv"

output_path = "D:\\share\\ตบ\\TRN_EXPENSE_2022\\"
output_file = "CO_202210_DATA.csv"

print("start =", datetime.now())

data = pd.read_csv(input_path + input_file)
cost_type = pd.read_csv(master_path + cost_type_co_master, encoding= 'UTF-8')
acc_category = pd.read_csv(master_path + accounting_category_co_master, encoding= 'TIS-620')

df = pd.DataFrame(data, columns= ['BUSINESS_PROCESS_CODE'])
Activity = df['BUSINESS_PROCESS_CODE'].str[-5:]
# https://datatofish.com/left-right-mid-pandas/

# print(Activity)

data['Activity'] = Activity
# https://www.delftstack.com/howto/python-pandas/pandas-create-column-based-on-other-columns/


# data.rename(columns={'Activity': 'Activity_Type'}, inplace=True)
print(data.head())
print(cost_type.head())




data['GL_CODE'] = data['GL_CODE'].astype(str)
acc_category['GL_CODE'] = acc_category['GL_CODE'].astype(str)

data = pd.merge(
    data,
    acc_category,
    left_on = ['GL_CODE'],
    right_on = ['GL_CODE'],
    how = 'left'
    )

data = pd.merge(
    data,
    cost_type,
    left_on = ['Activity'],
    right_on = ['Activity'],
    how = 'left'
    )

del data['Activity_Name']
data.rename(columns={'COST_TYPE': 'ประเภทต้นทุน'}, inplace=True)

# data['ประเภทต้นทุน'] = ''
data.loc[data['หมวดบัญชี'] == 'C17 ค่าใช้จ่ายอื่น', 'ประเภทต้นทุน'] = 'ค่าใช้จ่ายอื่น'
data.loc[data['หมวดบัญชี'] == 'C18 ต้นทุนทางการเงิน-ด้านการดำเนินงาน', 'ประเภทต้นทุน'] = 'ค่าใช้จ่ายอื่น'

print(data.head())


data.to_csv(output_path + output_file, index=False)
print("end =", datetime.now())

print()
print("error checking...")

print("start =", datetime.now())

data = pd.read_csv(output_path + output_file)

bool_series = pd.isnull(data['ประเภทต้นทุน'])
print(data[bool_series])
bool_series = pd.isnull(data['หมวดบัญชี'])
print(data[bool_series])

print("end =", datetime.now())
