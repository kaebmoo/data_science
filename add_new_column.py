# YEAR,MONTH,PRODUCT_KEY,BUSINESS_PROCESS_CODE,GL_CODE,EXPENSE_VALUE
# 2022,7,181050011,1R00000N0404,8160110101,0.59
# 2022,7,181050011,1R00000N0408,8160110101,6.14
# 2022,7,181050011,1R00000N0419,8160110101,1.25
# 2022,7,181050012,1C00400N0101,8160110101,6.25
# 2022,7,181050012,1C00400N0202,8160110101,46.01

import pandas as pd

data = pd.read_csv('D:\share\ตบ\TRN_EXPENSE_2022\CO_202207_EXAMPLE.csv')
cost_type = pd.read_csv('D:\share\master\COST_TYPE_CO_MASTER.csv', encoding= 'UTF-8')
acc_category = pd.read_csv('D:\share\master\ACCOUNTING_CATEGORY_CO_MASTER.csv', encoding= 'TIS-620')

df = pd.DataFrame(data, columns= ['BUSINESS_PROCESS_CODE'])
Activity = df['BUSINESS_PROCESS_CODE'].str[-5:]
# https://datatofish.com/left-right-mid-pandas/

print(Activity)

data['Activity'] = Activity
# https://www.delftstack.com/howto/python-pandas/pandas-create-column-based-on-other-columns/


# data.rename(columns={'Activity': 'Activity_Type'}, inplace=True)
print(data)
print(cost_type.head())

data = pd.merge(
    data,
    cost_type,
    left_on = ['Activity'],
    right_on = ['Activity'],
    how = 'left'
    )

del data['Activity_Name']
data.rename(columns={'COST_TYPE': 'ประเภทต้นทุน'}, inplace=True)
data['GL_CODE'] = data['GL_CODE'].astype(str)
acc_category['GL_CODE'] = acc_category['GL_CODE'].astype(str)

data = pd.merge(
    data,
    acc_category,
    left_on = ['GL_CODE'],
    right_on = ['GL_CODE'],
    how = 'left'
    )

print(data)

data.to_csv('D:\share\ตบ\TRN_EXPENSE_2022\CO_202207_EXAMPLE_OUTPUT.csv', index=False)