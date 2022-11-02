# Merging All
# https://www.geeksforgeeks.org/how-to-merge-multiple-csv-files-into-a-single-pandas-dataframe/
# importing libraries

import pandas as pd
import glob
import os
  
input_path = 'C:\\Report\\Data\\Sales Performance\\2022\\'
output_path = 'C:\\Report\\Data\\Sales Performance\\2022\\'
input_file = 'EXCEL_SPv4_2022*.csv'
output_file = 'SPv4_2022.csv'  

# merging the files
joined_files = os.path.join(input_path, input_file)
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
print(joined_list)

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

df['TIME_KEY_SAS'] = pd.to_datetime(df['TIME_KEY_SAS'], format='%d%b%Y')

print(df.head)
    
df.to_csv(output_path + output_file, index=False) # เขียนผลลัพธ์ ลงไฟล์ 
