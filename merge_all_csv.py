# Merging All
# https://www.geeksforgeeks.org/how-to-merge-multiple-csv-files-into-a-single-pandas-dataframe/
# importing libraries

import pandas as pd
import glob
import os

input_path = "D:\\share\\ตบ\\TRN_EXPENSE_2022\\"
input_files = "CO_2022*.csv"
output_path = "D:\\share\\ตบ\\TRN_EXPENSE_2022\\"
output_file = "CO__2022.csv"
  
# merging the files
joined_files = os.path.join(input_path, input_files)
print(joined_files)
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df.head)

df.to_csv(output_path + output_file, index=False) # เขียนผลลัพธ์ ลงไฟล์ 
