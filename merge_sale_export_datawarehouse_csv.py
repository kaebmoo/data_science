# Merging All
# https://www.geeksforgeeks.org/how-to-merge-multiple-csv-files-into-a-single-pandas-dataframe/
# importing libraries

import pandas as pd
import glob
import os

input_path = 'D:\\share\\data\\data_warehouse\\sale_performance\\'
output_path = 'D:\\share\\data\\data_warehouse\\sale_performance\\'
input_file = 'EXPORT_SP_202*.csv'
output_file = 'EXPORT_SP_.csv'  
# merging the files
joined_files = os.path.join(input_path, input_file)
  
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

df = pd.concat((pd.read_csv(f, encoding='cp874', sep="|") for f in joined_list), ignore_index=True)

# Finally, the files are joined
# df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)

# https://datatofish.com/strings-to-datetime-pandas/
df['TIME_KEY_DATE'] = pd.to_datetime(df['TIME_KEY_DATE'], format='%d%b%Y')

print(df.head)

df.to_csv(output_path + output_file, index=False) # เขียนผลลัพธ์ ลงไฟล์ 
