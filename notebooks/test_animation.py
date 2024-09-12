# %%
from dbnomics import fetch_series
import pandas as pd
import plotly_express as px
from scipy.__config__ import show
import numpy as np

#%%
#TEST ANIMATION WITH PX.LINE
maa_debt_percent = fetch_series('INSEE/DETTE-TRIM-APU-2014/T.DETTE_MAASTRICHT.S13.F.PROPORTION.FE.POURCENT.BRUT.2014.FALSE')
dfi = maa_debt_percent[['period', 'original_value']] 
# %%
dfi["period"] = pd.to_datetime(dfi["period"]).dt.strftime("%Y-%m")
start = 0
obs = len(dfi)
print(dfi.head)

#%%
df = pd.DataFrame()
for i in np.arange(start,obs):
    dfa = dfi.head(i).copy()
    dfa['frame'] = i
    df = pd.concat([df, dfa])

print(dfi.columns)
print(df.head)
#%%
fig = px.line(
        df,
        x='period',
        y='original_value',
        animation_frame = 'frame',
        title="Evolution of French General Government Debt by Quarter (% of GDP)",
    )
fig.layout.updatemenus[0].buttons[0]['args'][1]['frame']['redraw'] = True

fig.show()
# %%
