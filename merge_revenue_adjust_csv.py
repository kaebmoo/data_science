# Merging All
# https://www.geeksforgeeks.org/how-to-merge-multiple-csv-files-into-a-single-pandas-dataframe/
# importing libraries

import pandas as pd
import glob
import os

files = ["TRN_MANUALFI_SP_REBATE", "TRN_MANUALFI_SP_SAP_ADJUST_MY", "TRN_MANUALFI_SP_USAGE", \
         "TRN_PREPAID_CARD", "TRN_PREPAID_CARD_MY", "TRN_REFUND_ADJUST"]
path_files = ["D:\\share\\จบ\\จบง.ปี2565\\TRN_MANUALFI_SP_REBATE\\", "D:\\share\\จบ\\จบง.ปี2565\\TRN_MANUALFI_SP_SAP_ADJUST_MY\\", \
                  "D:\\share\\จบ\\จบง.ปี2565\\TRN_MANUALFI_SP_USAGE\\", "D:\\share\\จบ\\จบง.ปี2565\\TRN_PREPAID_CARD\\", \
                  "D:\\share\\จบ\\จบง.ปี2565\\TRN_PREPAID_CARD_MY\\", "D:\\share\\จบ\\จบง.ปี2565\\TRN_REFUND_ADJUST\\"]
output_path = "D:\\share\\จบ\\จบง.ปี2565\\REVENUE_ADJUST\\"
# merging the files
index = 0
for path in path_files:
    joined_files = os.path.join(path, "*.csv")
    print(joined_files)
  
    # A list of all joined files is returned
    joined_list = glob.glob(joined_files)
  
    # Finally, the files are joined
    df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
    print(df.head)

    df.to_csv(output_path + files[index] + ".csv", index=False) # เขียนผลลัพธ์ ลงไฟล์ 
    index += 1
    
print("Done")