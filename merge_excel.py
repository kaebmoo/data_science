import pandas as pd

df1 = pd.read_excel('C:\DW\TRN_EXPENSE_BEFORE_20220630.xlsx')
df2 = pd.read_excel('C:\DW\TRN_EXPENSE_BEFORE_20220731.xlsx')

df = pd.concat([df1,df2], axis=0, join='outer')

print(df.head)

df.to_excel("C:\DW\TRN_EXPESNE_BEFORE_EXCEL_2022.xlsx", sheet_name='2022-TRN_EXPENSE_BEFORE',
            index=False)  