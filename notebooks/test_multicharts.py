#%%
import pandas as pd
import numpy as np
import plotly.express as px
from dbnomics import fetch_series
import plotly.graph_objects as go

#%%
# input data
gov_rev = fetch_series("Eurostat/gov_10a_main/A.MIO_EUR.S13.TR.FR")

gov_expend = fetch_series("Eurostat/gov_10a_main/A.MIO_EUR.S13.TE.FR")
gov_expend["value"] = gov_expend["value"] * -1
print(gov_expend.head())

#%% 
#transform data for new dataset

df_rev = gov_rev[["original_period", "value"]].rename(columns={"value": "revenue"})
df_exp = gov_expend[["original_period", "value"]].rename(columns={"value": "expenditure"})

print(df_rev.head())
print(df_exp.head())


# %%
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x= df_rev["original_period"],
        y= df_rev["revenue"],
        marker_color = "limegreen",
        name= "Revenue"
    )
)
fig.add_trace(
    go.Bar(
        x = df_exp["original_period"],
        y = df_exp["expenditure"],
        marker_color = "darkblue",
        name= "Expenditure"
    )
)
fig.show()
# %%
