import pandas as pd # นำเข้า library pandas

data = pd.read_csv('C:\DW\TRN_EXPENSE_BEFORE_20220731.csv') # อ่านไฟล์ ไปไว้ตัวแปร data
lookup = pd.read_csv('C:\DW\EXPENSE_GL_CODE_NT1_NT.csv', encoding= 'tis-620') # อ่านไฟล์ ไปไว้ใน lookup

# print(df.to_string()) 
# print(df)

print(data.head()) # พิมพ์ โครงสร้างไฟล์ data ออกมาดู
print(lookup.head())

# dg['GL_CODE_NT1'] = dg['GL_CODE_NT1'].astype(int)
data['GL_CODE'] = data['GL_CODE'].astype(str) # เปลี่ยน column GL_CODE ให้เป็น string
data.rename(columns={'GL_CODE': 'GL_CODE_NT1'}, inplace=True) # เปลี่ยนชื่อ column GL_CODE เป็น GL_CODE_NT1

# ทำการ merge หรือ การทำแบบ vlookup ของ excel / left join
merged = pd.merge(
    data,
    lookup,
    left_on = ['GL_CODE_NT1'],
    right_on = ['GL_CODE_NT1'],
    how = 'left'
    )

print(merged.head())

del merged['GL_CODE_NT1'] # ลบ column GL_CODE_NT1
del merged['GL_NAME_NT1']

print(merged.head())

merged.to_csv('C:\DW\merged_output.csv', index=False) # เขียนผลลัพธ์ ลงไฟล์ 

# help me
# https://note.nkmk.me/en/python-pandas-dataframe-rename/#:~:text=You%20can%20use%20the%20rename,change%20column%2Findex%20name%20individually.&text=Specify%20the%20original%20name%20and,is%20for%20the%20index%20name.
# https://www.statology.org/you-are-trying-to-merge-on-object-and-int64-columns/
# https://betterprogramming.pub/vlookups-are-cancelled-why-python-pandas-are-a-much-better-way-to-merge-data-dbce0126166a
# https://datagy.io/vlookup-in-python-and-pandas-using-map-or-merge/
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
# https://www.educative.io/answers/how-to-delete-a-column-in-pandas
