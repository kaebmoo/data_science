# Merging All
# https://www.geeksforgeeks.org/how-to-merge-multiple-csv-files-into-a-single-pandas-dataframe/
# importing libraries

import pandas as pd
import glob
import os
from datetime import datetime
  
# merging the files
joined_files = os.path.join("D:\share\ตบ\TRN_EXPENSE_2022", "072022_Data_TRN_EXPENSE_*.xlsx")
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)

# datetime object containing current date and time
# now = datetime.now()
 
print("start =", datetime.now())
  
# Finally, the files are joined
df = pd.concat(map(pd.read_excel, joined_list), ignore_index=True)
print(df.head)

df.to_csv('C:\DW\072022_Data_TRN_EXPENSE.csv', index=False) # เขียนผลลัพธ์ ลงไฟล์ 

print("end =", datetime.now())