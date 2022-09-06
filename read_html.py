# https://pbpython.com/pandas-html-table.html

import pandas as pd
import numpy as np
from unicodedata import normalize

table = pd.read_html("inquiry.html")

print(f'Total tables: {len(table)}')

df = table[0]
print(df.head())
print()
print(df.info())

print(df[df.PERIOD == "2022/01"])

print(df.query('PERIOD == "2022/01" and PROCESS == "completed"'))
row = df.query('PERIOD == "2022/01"')
print(row.PAID_AMOUNT)

print()
print(row.PAID_AMOUNT+1)