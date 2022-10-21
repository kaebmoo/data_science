import pandas as pd

# pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_excel("C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\data\\topup_data_test.xlsx")

print(df)

# df.loc["DIV"] = df.loc[df["FLAG"] == 1, "REVENUE_TOTAL"]
print(df.loc[df['FLAG'] == 1])
print(df.loc[df['FLAG'] == 0])
R1 = df.loc[df['FLAG'] == 1]
R2 = df.loc[df['FLAG'] == 0]
R1.rename(columns={"REVENUE_TOTAL":"R1", "FLAG" : "F1"}, inplace=True)
R2.rename(columns={"REVENUE_TOTAL":"R2", "FLAG" : "F2"}, inplace=True)
R1 = R1.reset_index(drop=True)
R2 = R2.reset_index(drop=True)
print(R1)
print(R2)

R3 = pd.merge(R1, R2, on="COST_CENTER_DEPARTMENT")
print(R3)
R3["FACTOR"] = R3.loc[:,"R1"] / R3.loc[:,"R2"]
print(R3)