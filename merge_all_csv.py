# Merging All
# https://www.geeksforgeeks.org/how-to-merge-multiple-csv-files-into-a-single-pandas-dataframe/
# importing libraries

import pandas as pd
import glob
import os
  
# merging the files
joined_files = os.path.join("C:\\DW", "TRN_EXPENSE_BEFORE_2022*.csv")
print(joined_files)
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df.head)

df.to_csv('C:\DW\TRN_EXPENSE_BEFORE_NT1_2022.csv', index=False) # เขียนผลลัพธ์ ลงไฟล์ 
