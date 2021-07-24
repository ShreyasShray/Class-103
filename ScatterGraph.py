import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

scatter_chart = px.scatter(df, x = "Country", y = "Per capita", size = "Percentage", size_max = 40, color = "Country")
scatter_chart.show()