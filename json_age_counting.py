import requests
import numpy as np
import pandas as pd
from pandas import json_normalize


r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
print(len(r.json()['data']))
print(r.json()['data'])
# json_data = "key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"

data_ = [data.split('=')[1] for data in r.json()['data'].split(',')]
# data_ = [data.split('=')[1] for data in json_data.split(',')]
# print(data_)

df = pd.DataFrame.from_dict({'age': data_[1::2], 'key': data_[::2]})
# print(df)
print(df['age'])
df.to_csv('age_counting.csv')
df['age'] = df['age'].astype(int)
flag = df['age'] >= 50
# print(df.dtypes)
print(flag)
num_rows = len(flag[flag == True].index)
print(num_rows)