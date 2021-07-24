import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

bar_graph = px.bar(df, x = "Country", y = "InternetUsers", title = "Internet Users")

bar_graph.show()