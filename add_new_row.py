import pandas as pd

df = pd.read_excel("challenge.xlsx")

newtable = pd.DataFrame()
newtable["First Name"] = ""
newtable["Last Name"] = ""
newtable["Phone"] = ""

print(df)
print(newtable)

df = df.reset_index()

for index, person in df.iterrows():
    firstname = person["First Name"]
    lastname = person["Last Name "]
    phone = str(person["Phone Number"])
    print(firstname[0] + " " + firstname + " " + lastname + " " + phone)
    if firstname[0] == "J":
        print()
        newtable.loc[len(newtable.index)] = [firstname, lastname, phone]
        
        # or
        
        # df1 = pd.DataFrame({"First Name": [firstname], "Last Name": [lastname], "Phone": [phone]})
        # print(df1)
        # newtable = pd.concat([newtable, df1])
        
    # print(person)
    
print(newtable)