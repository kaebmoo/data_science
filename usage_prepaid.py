import pandas as pd


# ข้อมูลรายงานที่เรียกจาก SAP เป็นไฟล์แบบ csv ถ้าเป็น excel ให้แปลงมาเป็น csv ก่อน
data_file = "C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\data\\rev_prepaid.csv"

# input = pd.read_excel("C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\data\\rev08_1.xlsx")
df_prepaid = pd.read_csv(data_file, encoding="tis-620",
                converters={"เลขที่เอกสาร":str, "ผลิตภัณฑ์/บริการ":str, "ที่ประกอบธุรกิจ":str, "งวดการผ่านรายการ":str, "ปีบัญชี":str})

df_revenue = pd.read_csv("C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\data\\rev08_1.csv",
                        encoding="tis-620", converters={"เลขที่เอกสาร":str,"ผลิตภัณฑ์/บริการ":str, "บัญชี":str})
#df = pd.read_excel("rev08_1.xlsx", converters={"เซกเมนต์":str,"ผลิตภัณฑ์/บริการ":str})

# https://stackoverflow.com/questions/47333227/pandas-valueerror-cannot-convert-float-nan-to-integer
year_revenue = df_revenue["วันที่ผ่านรายการ"].str[-4:]
year_revenue = pd.to_numeric(year_revenue, errors='coerce')
year_revenue = str(int(year_revenue.max()))
month_revenue = str(int(df_revenue["งวดการผ่านรายการ"].max()))
print(year_revenue)
print(month_revenue)
print()
year = str(int(df_prepaid["ปีบัญชี"].max()))
month = str(int(df_prepaid["งวดการผ่านรายการ"].max()))
print(year)
print(month)

if (year_revenue != year) or (month_revenue != month):
    print("งวดรายงาน Prepaid & Revenue ไม่ตรงกัน")
    exit()

df_prepaid.rename(columns={"ผลิตภัณฑ์/บริการ": "PRODUCT_KEY_PREPAID"}, inplace=True)
df_revenue.rename(columns={"ผลิตภัณฑ์/บริการ": "PRODUCT_KEY_REVENUE"}, inplace=True)
df_revenue.rename(columns={"จำนวนในสกุลเงินในประเทศ": "REVENUE_VALUE"}, inplace=True)
df_revenue.rename(columns={"ศูนย์ต้นทุน": "COST_CENTER"}, inplace=True)

# https://www.statology.org/pandas-keep-columns/
df_prepaid = df_prepaid[["PRODUCT_KEY_PREPAID", "เลขที่เอกสาร"]]
df_revenue = df_revenue[["PRODUCT_KEY_REVENUE", "เลขที่เอกสาร", "ข้อความ", "REVENUE_VALUE", "COST_CENTER"]]
# ลบเครื่องหมาย , ในข้อความตัวเลขออก https://stackoverflow.com/questions/28986489/how-to-replace-text-in-a-string-column-of-a-pandas-dataframe
df_revenue["REVENUE_VALUE"] = df_revenue["REVENUE_VALUE"].replace(",", "", regex=True)
# แปลงข้อความเป็นเลข
df_revenue["REVENUE_VALUE"] = pd.to_numeric(df_revenue["REVENUE_VALUE"])
# คูณ ด้วย -1
df_revenue["REVENUE_VALUE"] = df_revenue["REVENUE_VALUE"] * -1

# https://sparkbyexamples.com/pandas/pandas-drop-rows-with-condition/
df1 = df_revenue[df_revenue["ข้อความ"].str[0:3] == "US:"]
df2 = df_revenue[df_revenue["ข้อความ"].str[0:3] == "EX:"]
print(df1)
print(df2)

df_revenue = pd.concat([df1, df2], ignore_index=True)
print(df_revenue.head())

# https://www.datacamp.com/tutorial/joining-dataframes-pandas
df_usage_prepaid = pd.merge(df_revenue, df_prepaid, on="เลขที่เอกสาร", how="inner") 
df_usage_prepaid["YEAR"] = year
df_usage_prepaid["MONTH"] = month
df_usage_prepaid = df_usage_prepaid[["YEAR", "MONTH", "PRODUCT_KEY_PREPAID", "PRODUCT_KEY_REVENUE", "REVENUE_VALUE", "COST_CENTER"]]

print("Usage prepaid")
df_usage_prepaid.to_csv('usage_prepaid.csv', index=False)


print()
print("Done")