import pandas as pd
from datetime import datetime

input_path = "C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\data\\arap\\"
output_path = "C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\data\\arap\\"
master_customer_file = "master_customergroup.xlsx"
master_ba_tot_file = "ba_tot.xlsx"
invoice_file = "INV_SUM_SAP_IBACSS_202001.csv"
balance_receivable_file = "balance_receivable_data.csv"
invoice_summary_output = "invoice_sum_ba.csv"
balance_receivable_output = "balance_receivable_output.csv"

print("start =", datetime.now())

df_master_ba = pd.read_excel(input_path + master_ba_tot_file, \
                          converters={ "CONTRNO":str, "CUSTOMER_GROUP":str})

df_invoice = pd.read_csv(input_path + "invoice_sum.csv", converters={ "CONTRNO":str, "CUSTOMER_GROUP":str})
print(df_master_ba)
print(df_invoice)
df_output = df_master_ba[df_master_ba["CONTRNO"].isin(df_invoice["CONTRNO"])]["CUSTOMER_GROUP"].values
print(df_output)
mask = df_invoice[df_invoice["CONTRNO"].isin(df_master_ba["CONTRNO"])].index
print(mask)
df_invoice.loc[mask, "CUSTOMER_GROUP"] = "201"

df_invoice.to_csv(output_path + invoice_summary_output, index=False, float_format="%.2f")

print("end =", datetime.now())