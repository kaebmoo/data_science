# https://kanoki.org/2019/07/04/pandas-difference-between-two-dataframes/

import pandas as pd

df1 = pd.read_csv("dw_cc_map.csv")
df2 = pd.read_csv("me_cc_map.csv")


df = pd.concat([df1,df2]).drop_duplicates(keep=False)
print(df)

df.to_csv('cc_diff.csv', index=False)