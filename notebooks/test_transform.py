#%%
from dbnomics import fetch_series
import plotly.graph_objects as go
import plotly_express as px
import pandas as pd
#load data
house_holds = fetch_series(
    [
        "OECD/NAAG/FRA.DBTS14_S15NDI",
        "OECD/DP_LIVE/FRA.HHSAV.TOT.PC_HHDI.A"
    ]
)
#%%
house_holds = house_holds[house_holds["original_period"] >= "1995"]
print(house_holds)
hh_data = house_holds[house_holds["original_period"] >= "1995"]

#%%

house_debt = fetch_series("BDF/DWA1/Q.FR.S14._Z._Z.ADA._Z.PT.S.N")
house_saving = fetch_series("OECD/DP_LIVE/FRA.HHSAV.TOT.PC_HHDI.A")

#%%
df_debt = house_debt[["original_period", "original_value","series_name"]].rename(
    columns= {"France, Households, Debts to Assets ratio": "debt"}
)
print(df_debt)

#%%
df_saving = house_saving[["original_period", "original_value","series_name"]].rename(
    columns= {"France – Household savings – Total – % of household disposable income – Annual": "saving"}
)

print(df_saving)

# %%


#%%
labels = {
    "France – Debt of households, percentage of net disposable income":"Debt of household (% of dispoanle income)",
    "France – Household savings – Total – % of household disposable income – Annual":"Household savings (% of disposable income)"
}

fig = px.bar(
    house_holds, 
    x = "series_name", 
    y = "original_value",
    animation_frame = "original_period",
    animation_group = "series_name",
    color = "series_name",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title = "Debt vs Savings"
)

fig.update_layout(
    xaxis = dict(
        tickvals=list(labels.keys()),
        ticktext =list(labels.values())
    ),
    xaxis_title= "",
    yaxis_title = "",
    showlegend=False
)

fig.show()
# %%
