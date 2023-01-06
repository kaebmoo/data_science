import plotly.graph_objects as go
import pandas as pd

label_file = pd.read_csv("D:\\DB\\QPR\\label.csv")
label_data = label_file['LABEL'].tolist()
# print(label_data)

source_target_file = pd.read_csv("D:\\DB\\QPR\\source_target.csv")
source_data = source_target_file['SOURCE'].tolist()
target_data = source_target_file['TARGET'].tolist()
value_data = source_target_file['VALUE'].tolist()
# print(source_data)

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = label_data, # ["A1", "A2", "B1", "B2", "C1", "C2"]
      color = "blue"
    ),
    link = dict(
      source = source_data, # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = target_data,
      value = value_data
  ))])

fig.update_layout(title_text="QPR Layer Diagram", font_size=10)
fig.show()