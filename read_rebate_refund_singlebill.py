import pandas as pd

# input = pd.read_excel("C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\data\\rev08_1.xlsx")
df = pd.read_csv("C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\data\\rev08_1.csv", encoding="tis-620",
                 converters={"เซกเมนต์":str,"ผลิตภัณฑ์/บริการ":str})
# df = pd.read_excel("C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\data\\rev08_1.xlsx",
#                 converters={"เซกเมนต์":str,"ผลิตภัณฑ์/บริการ":str})

with open("refund.csv", "w") as output:
    output.write("SEGMENT,PRODUCT_KEY,COST_CENTER,REVENUE_VALUE\n")

# คัดเฉพาะข้อความ 6 ตัวแรก
ref = df["ข้อความ"].str[0:6]
# print(ref)

index = 0
for row in df["ข้อความ"]:
    # if row.str[:6] == "AJ:B2." :
    #   print("Refund")
    row_data = str(row)
    if row_data[0:6] == "AJ:B2.":
        revenue = float(str(df.loc[index, "จำนวนในสกุลเงินในประเทศ"]).replace(",", ""))
        refund_value = str(revenue)
        cost_center = df.loc[index, "ศูนย์ต้นทุน"]
        segment = df.loc[index, "เซกเมนต์"]
        product_key = df.loc[index, "ผลิตภัณฑ์/บริการ"]
        print(segment, end="\t")
        print(product_key, end="\t")
        print(cost_center, end="\t")
        print(refund_value)
        with open("refund.csv", "a") as output:
            output.write(segment+","+product_key+","+cost_center+","+refund_value+"\n")
    index = index + 1

index = 0
for row in df["ข้อความส่วนหัวเอกสาร"]:
    row_data = str(row)
    if row_data == "Billing:SG":
        revenue = float(str(df.loc[index, "จำนวนในสกุลเงินในประเทศ"]).replace(",", "")) * -1
        revenue_value = str(revenue)
        print(revenue_value)
    index = index + 1