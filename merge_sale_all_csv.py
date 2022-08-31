# Merging All
# https://www.geeksforgeeks.org/how-to-merge-multiple-csv-files-into-a-single-pandas-dataframe/
# importing libraries

import pandas as pd
import glob
import os
  
# merging the files
joined_files = os.path.join("C:\\Report\\Data\\Sales Performance\\2022", "EXCEL_SPv4_2022*.csv")
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)

# with open('C:\\Report\\Data\\Sales Performance\\2022\\EXCEL_SPv4_2022-1.csv') as t:
#    print(t)
    
# print(joined_list)

#li = []

#for filename in joined_list:
#        df = pd.read_csv(filename, ignore_index=True, encoding='TIS-620')
#        li.append(df)
# frame = pd.concat(li, axis=0, ignore_index=True)

df = pd.concat((pd.read_csv(f, encoding='cp874') for f in joined_list), ignore_index=True)

# Finally, the files are joined
# df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)

print(df.head)

df.to_csv('C:\\Report\\Data\\Sales Performance\\2022\SPv4_2022.csv', index=False) # เขียนผลลัพธ์ ลงไฟล์ 
