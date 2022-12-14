# https://kanoki.org/2019/07/04/pandas-difference-between-two-dataframes/

import pandas as pd

df1 = pd.read_csv("C:\\dwdata\\bak\\TRN_PREPAID_CARD_DATA_202211_AR.csv")
df2 = pd.read_csv("C:\\dwdata\\TRN_PREPAID_CARD_DATA_202211.csv")


df = pd.concat([df1,df2]).drop_duplicates(keep=False)
print(df)

df.to_csv('D:\\tmp\\prepaid_card_data_diff.csv', index=False)