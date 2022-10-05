import pandas as pd
import numpy as np
studentdetails = {
       "studentname":["Ram","Sam","Scott","Ann","John"],
       "mathantics" :[80,90,85,70,95],
       "science" :[85,95,80,90,75],
       "english" :[90,85,80,70,95]
              }
index_labels=['r1','r2','r3','r4','r5']
df = pd.DataFrame(studentdetails ,index=index_labels)

# Use DataFrame.sum() method
df2 = df['mathantics'].sum()
print(df2)

# Using DataFrame.sum() method 
df2 = sum(df['mathantics'])
print(df2)

df.loc['total'] = df.sum(axis=0, numeric_only = True)
print(df)

# Use DataFrame.loc[] and pandas.Series() to get total of columns
df.loc['Total'] = pd.Series(df['mathantics'].sum(), index = ['mathantics'])
print(df)

# Get total of columns using DataFrame.loc[] method
df.loc['Total'] = df["mathantics"].sum()
print(df)

# Use DataFrame.loc[] & DataFrame.sum() Method
df.loc["Total", "mathantics"] = df.mathantics.sum()
print(df)

# Use DataFrame.at[] method to get total of columns
df.at['Total', "mathantics"] = df["mathantics"].sum()
print(df)

# Use DataFrame.append() method
df2 = df.append(pd.DataFrame(df.mathantics.sum(), index = ["Total"], columns=[ "mathantics"]))
print(df2)