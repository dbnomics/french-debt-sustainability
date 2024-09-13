#Add to dashboard and add comments
#%%
from dbnomics import fetch_series
import plotly.graph_objects as go
import plotly_express  as px 
import pandas as pd
#%%
df1 = fetch_series("Eurostat/ei_mfir_m/M.NSA.NAP.MF-LTGBY-RT.FR")
df2 = fetch_series("OECD/MEI/FRA.NAEXKP01.GYSA.A")
#%%
df3 = fetch_series("Eurostat/irt_lt_mcby_a/A.MCBY.FR")

#%%
nwdf3 = df3[["original_period", "series_name","original_value"]].rename(
    columns={
        "original_value" : "bond yields"
    }
)

nwdf2 = df2[["original_period", "series_name","original_value"]].rename(
    columns={
        "original_value" : "economic growth rate"
    }
)

print(nwdf3)
print(nwdf2)
#%%
df = pd.merge(nwdf3, nwdf2, on= "original_period")
print(df)

#%%
df["Gap"] = df["bond yields"] - df["economic growth rate"]
df["original_period"] = pd.to_datetime(df["original_period"]).dt.strftime("%Y-%m")
print(df)
#%%
#plot both 
fig = go.Figure()

fig.add_trace(
    go.Line(
        x = df1["original_period"],
        y = df1["original_value"], 
        line = dict(color = "darkblue"), 
        name = "Long term government bond yields"
    )
)

fig.add_trace(
    go.Line(
        x = df2["original_period"], 
        y = df2["original_value"], 
        line = dict(color = "limegreen"), 
        name = "Economics Growth rate"
    )
)

fig.show()
# %%
#plot r - g 

fig = go.Figure()

fig.add_trace(
    go.Line(
        x = df["original_period"],
        y = df["Gap"], 
        line = dict(color = "blueviolet")
    )
)

fig.show()

# %%
