# https://kanoki.org/2019/07/04/pandas-difference-between-two-dataframes/

import pandas as pd

df1 = pd.read_csv("c:\\dw\\TRN_REVENUE_NT2_20221031_DW.csv")
df2 = pd.read_csv("c:\\dw\\TRN_REVENUE_NT2_20221031.csv")


df = pd.concat([df1,df2]).drop_duplicates(keep=False)
print(df)

df.to_csv('C:\\DW\\revenue_202210_diff.csv', index=False)