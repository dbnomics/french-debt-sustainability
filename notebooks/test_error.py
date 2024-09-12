#%%
from dbnomics import fetch_series

#%%
df1 = fetch_series("OECD/NAAG/FRA.DBTS14_S15NDI")
df2 = fetch_series("OECD/DP_LIVE/FRA.HHSAV.TOT.PC_HHDI.A")

#%%
df = fetch_series(
    [
        "OECD/NAAG/FRA.DBTS14_S15NDI",
        "OECD/DP_LIVE/FRA.HHSAV.TOT.PC_HHDI.A"
    ]
)
# %%
