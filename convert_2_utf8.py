import pandas as pd

df_org = pd.read_csv("D:\\share\master\\MASTER_ORGANIZATION_NT1.5.csv", encoding="tis-620")
df_product = pd.read_csv("D:\\share\master\\MASTER_PRODUCT_NT.csv", encoding="tis-620", sep="\t", lineterminator='\r')

df_org.to_csv("D:\\share\master\\MASTER_ORGANIZATION_NT1.5_UTF8.csv")
df_product.to_csv("D:\\share\master\\MASTER_PRODUCT_NT_UTF8.csv")