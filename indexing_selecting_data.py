# importing pandas package
import pandas as pd
  
# making data frame from csv file
data = pd.read_csv("nba-2.csv", index_col ="Name")
  
# retrieving row by loc method
first = "A"
# second = data.loc["R"]

if first in data.index:
    first = data.loc["A"]
    print(first, "\n\n\n")
else:
    print("Not found.")