import pandas as pa
import plotly.express as px
import plotly.figure_factory as pf

df= pa.read_csv("data 2.csv")
fig=pf.create_distplot([df["Weight(Pounds)"].tolist()],["weight"],show_hist=True)
fig.show()