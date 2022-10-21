import pandas as pd

import glob
import os
  
# merging the files
joined_files = os.path.join("D:\\share\\ตบ\\TRN_Revenue_2022", "TRN_REVENUE_ADJ_*.csv")
# print(joined_files)
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
# print(joined_list)

files = pd.DataFrame(joined_list)
# print(files)

substring = "gl"
mask = files.applymap(lambda x: substring in x.lower() if isinstance(x,str) else False).to_numpy()
# print(mask)
# print(files.loc[mask,0])

files.drop(files.loc[mask,0].index, axis=0, inplace=True)
print(files)


substring = "ytd"
mask = files.applymap(lambda x: substring in x.lower() if isinstance(x,str) else False).to_numpy()
files_ytd = files.loc[mask,0]
joined_list_ytd = files_ytd.values.tolist()
print(joined_list_ytd)

files.drop(files.loc[mask,0].index, axis=0, inplace=True)
print(files)
joined_list_month = files[0].values.tolist()
print(joined_list_month)

# TRN_REVENUE_ADJ_GL_

# Finally, the files are joined
# df = pd.concat(map(pd.read_csv, joined_list_ytd), ignore_index=True)
# print(df.head)
df = pd.DataFrame()
for filename in joined_list_ytd:
    data = pd.read_csv(filename, encoding="TIS-620")
    df = pd.concat([df, data], axis=0)
df.to_csv('C:\\DW\\TRN_REVENUE_ADJ_YTD_2022.csv', index=False) # เขียนผลลัพธ์ ลงไฟล์ 

df = pd.DataFrame()
for filename in joined_list_month:
    data = pd.read_csv(filename, encoding="TIS-620")
    df = pd.concat([df, data], axis=0)
df.to_csv('C:\\DW\\TRN_REVENUE_YTD_2022.csv', index=False)