# แปลง excel เป็น csv

import glob
import os
from datetime import datetime
from subprocess import call
import pandas as pd

script_excel2csv = 'C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\ExcelToCsv.vbs' # vb script program
path = "D:\\share\\จบ\\จบง.ปี2565\\Expense NT2\\" # data path excel files

print("start =", datetime.now())

joined_files = os.path.join(path, "*.xlsx")
print(joined_files)
joined_list = glob.glob(joined_files)
print(joined_list)
df = pd.DataFrame()
sheet = "1"
for file in joined_list:
    print(file)
    filecsv = file.replace("-new", "")
    filecsv = filecsv.replace(".xlsx", "")
    csv = filecsv + ".csv"
    print(csv)
    call(['cscript.exe', script_excel2csv, str(file), csv, sheet])

print("end =", datetime.now())