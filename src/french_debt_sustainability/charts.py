import pandas as pd
import plotly_express  as px 
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
"""
Ajouter les labels et les légendes aux graphiques 
"""

def plot_debt_percent(maa_debt_percent):

    dfi = maa_debt_percent[['period', 'original_value']]
    dfi["period"] = pd.to_datetime(dfi["period"]).dt.strftime("%Y-%m")
    start = 1
    obs = len(dfi)
    #create datastructure for animation
    df = pd.DataFrame()
    for i in np.arange(start,obs):
        dfa = dfi.head(i).copy()
        dfa['ix'] = i
        df = pd.concat([df, dfa])

    fig = px.line(
            dfi,
            x='period',
            y='original_value',
            color_discrete_sequence=['mediumslateblue'],
            title="French General Government Debt (% of GDP)",
        )


    fig.update_layout(
    height=650, 
    xaxis_title="Years",
    yaxis_title="General Government Debt (% of GDP)",
    )

    fig.update_layout(sliders=[{
    'currentvalue': {
        'prefix': "",  
        'font': {'size': 1}
    }     
    }]) 

    return fig 

def plot_debt(maa_debt):
    maa_debt["original_period"] = pd.to_datetime(maa_debt["original_period"]).dt.strftime("%Y-%m")
    dfi = maa_debt[['original_period', 'original_value']]
    dfi["original_period"] = pd.to_datetime(dfi["original_period"]).dt.strftime("%Y-%m")
    start = 0
    obs = len(dfi)
    #create datastructure for animation
    df = pd.DataFrame()
    for i in np.arange(start,obs):
        dfa = dfi.head(i).copy()
        dfa['ix'] = i
        df = pd.concat([df, dfa])
        
    
    fig = px.line(
            dfi,
            x='original_period',
            y='original_value',
            title="French General Government Debt",
            color_discrete_sequence=['darkblue'], 
        )
    fig.update_layout(
    height=650, 
    xaxis_title="Years",
    yaxis_title="General Government Debt)",
    )
    return fig

def plot_expenditures(expend):
    labels = {
        "01 - General public services":"General Public Service", 
        "02 - Defence":"Defence", 
        "03 - Public order and safety":"Public Order and Safety", 
        "04 - Economic affairs":"Economic affairs",
        "05 - Envirommental protection":"Environmental Protection", 
        "06 - Housing and community amenitis":"Housing and Community amenitis", 
        "07 - Health":"Health", 
        "08 - Recreation, culture and religion":"Recreation, culture and religion", 
        "09 - Education": "Education",
        "10 - Social protection": "Social Protection"
        }
    expend["original_period"] =pd.to_datetime(expend["original_period"]).dt.strftime("%Y")
    fig = px.bar(
        expend,
        x = "Categories",
        y = "value", 
        title="General Governement Expenditures by Sector",
        color = "Categories", 
        color_discrete_sequence=px.colors.qualitative.Pastel,
        animation_frame= "original_period",
        animation_group= "Categories", 
        text_auto=True

    )

    fig.update_layout(
        xaxis = dict(
            tickvals=list(labels.keys()),
            ticktext =list(labels.values())
        ),
        xaxis_title= "",
        yaxis_title = "Expenditures (in million)",
        showlegend=False
    )
    return fig 

def plot_expenditures_prop(original_expend):
    labels = {
        "01 - General public services":"General Public Service", 
        "02 - Defence":"Defence", 
        "03 - Public order and safety":"Public Order and Safety", 
        "04 - Economic affairs":"Economic affairs",
        "05 - Envirommental protection":"Environmental Protection", 
        "06 - Housing and community amenitis":"Housing and Community amenitis", 
        "07 - Health":"Health", 
        "08 - Recreation, culture and religion":"Recreation, culture and religion", 
        "09 - Education": "Education",
        "10 - Social protection": "Social Protection"
        }
    
    filtered_df  = original_expend[original_expend["Categories"] != "Total"]
    filtered_df["original_period"] =pd.to_datetime(filtered_df["original_period"]).dt.strftime("%Y")
    fig = px.bar(
        filtered_df,
        x = "Categories",
        y = "value", 
        color = "Categories", 
        animation_frame= "original_period",
        animation_group= "Categories",
        text_auto=True
    )
    fig.update_layout(height = 600)
    fig.update_layout(
        xaxis = dict(
            tickvals=list(labels.keys()),
            ticktext =list(labels.values())
        ),
        xaxis_title= "",
        yaxis_title = "Expenditures (%)",
        showlegend=False
    )
    return fig

def plot_pie_expenditures(original_expend): 
    df_2000 = original_expend[(original_expend['original_period'] == "2000") & (original_expend['Categories'] != "Total")]
    df_2020 = original_expend[(original_expend['original_period'] == "2020") & (original_expend['Categories'] != "Total")]

    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]], 
                    subplot_titles=['2000','2020'])

    fig.add_trace(go.Pie(labels=df_2000['Categories'], values=df_2000['value'], name="2000", marker_colors=px.colors.qualitative.Pastel), 1, 1)

    fig.add_trace(go.Pie(labels=df_2020['Categories'], values=df_2020['value'], name="2020", marker_colors=px.colors.qualitative.Pastel), 1, 2)

    fig.update_layout(
        title_text="Public Spending Repartion for 2000 & 2020",
        annotations=[dict( x=0.20, y=1, font_size=20, showarrow=False),
                     dict( x=0.80, y=1, font_size=20, showarrow=False)]
    )

    return fig 


def plot_expenditures_percentage(expend_percent):
    expend_percent["original_period"] =pd.to_datetime(expend_percent["original_period"]).dt.strftime("%Y")
    fig = px.bar(
        expend_percent,
        x = "Categories",
        y = "value", 
        color = "Categories", 
        animation_frame= "original_period",
        animation_group= "Categories",
    )
    fig.update_layout(height = 650)
    return fig 

def plot_expend_revenue(gov_rev, gov_expend):

    df_rev = gov_rev[["original_period", "value"]].rename(columns={"value": "revenue"})
    df_exp = gov_expend[["original_period", "value"]].rename(columns={"value": "expenditure"})
    df = pd.merge(df_rev,df_exp, on= "original_period")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = df["original_period"],
            y = df["revenue"],
            mode = "lines+markers", 
            name = "Revenue",
            line = dict(color = "limegreen")
        )
    )
    fig.add_trace(
        go.Scatter(
            x = df["original_period"],
            y = df["expenditure"],
           mode = "lines+markers", 
           name = "Expenditure", 
           line= dict(color = "darkblue")
        )
    )
    fig.update_layout(
        xaxis_title = "Years",
        yaxis_title = "The amount in thousands of millions"
    )
    return fig

def plot_chart_exp_rev(gov_rev, gov_expend):
    #downlaod data & transform expenditure in negative data
    df_rev = gov_rev[["original_period", "value"]].rename(columns={"value": "revenue"})
    df_exp = gov_expend[["original_period", "value"]].rename(columns={"value": "expenditure"})
    gov_expend["value"] = gov_expend["value"] * -1
    df_rev = gov_rev[["original_period", "value"]].rename(columns={"value": "revenue"})
    df_exp = gov_expend[["original_period", "value"]].rename(columns={"value": "expenditure"})

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x= df_rev["original_period"],
            y= df_rev["revenue"],
            marker_color = "limegreen",
            name= "Revenue "
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

    fig.update_layout(
        xaxis_title = "Years",
        yaxis_title = "The amount in thousands of millions"
    )
    return fig 

def plot_lng_rate(lng_rate):
    lng_rate["original_period"] == pd.to_datetime(lng_rate["original_period"]).dt.strftime("%Y-%m")
    lng_rate = lng_rate.rename(columns={"Geopolitical entity (reporting)": "Area"})
    
    fig = px.line(
        lng_rate, 
        x = "original_period",
        y = "original_value",
        color = "Area", 
        title = "French long term government bond yields"
    )

    fig.update_layout(
    height = 650,
    xaxis_title = "Years",
    yaxis_title = "Long Term Interest Rate (%)"
    )
    
    fig.update_traces(
    selector=dict(name = "Euro area (EA11-1999, EA12-2001, EA13-2007, EA15-2008, EA16-2009, EA17-2011, EA18-2014, EA19-2015, EA20-2023)"), name = "Euro Area"
    )
    return fig 

def plot_households_data(hh_df):
    new_hh_df= hh_df[hh_df["original_period"] >= "1995"]
    labels = {
    "France – Debt of households, percentage of net disposable income":"Debt of household (% of disposable income)",
    "France – Household savings – Total – % of household disposable income – Annual":"Household savings (% of disposable income)"
    }


    fig = px.bar(
        new_hh_df, 
        x = "series_name", 
        y = "original_value",
        animation_frame = "original_period",
        animation_group = "series_name",
        color = "series_name",
        color_discrete_sequence=px.colors.qualitative.Pastel,
        title = "Debt vs Savings",
        text_auto = True
    )

    fig.update_layout(
        xaxis = dict(
            tickvals=list(labels.keys()),
            ticktext =list(labels.values())
        ),
        xaxis_title= "",
        yaxis_title = "The amount in % of disposable income",
        showlegend=False,
        height = 650
    )
    return fig 

def plot_int_rate_vs_growth_rate(int_rate, growth_rate):
    df1= int_rate[["original_period", "series_name","original_value"]].rename(
    columns={
        "original_value" : "bond yields"
    }
    )

    df2 = growth_rate[["original_period", "series_name","original_value"]].rename(
        columns={
            "original_value" : "economic growth rate"
        }
    )

    df = pd.merge(df1, df2, on= "original_period")
    df["Gap"] = df["bond yields"] - df["economic growth rate"]

    # Créer une figure avec deux courbes : une pour les valeurs positives et une pour les négatives
    fig = go.Figure()

    # Courbe pour les valeurs positives (couleur par défaut ou personnalisée)
    fig.add_trace(
        go.Line(
            x=df["original_period"],
            y=df["Gap"],
            mode='lines',
            line=dict(color='orange'),  # Couleur bleue pour les valeurs positives
            name='Gap'
        )
    )

# Ajouter le titre
    fig.update_layout(
        title="Difference between Interest Rate and Economic Growth Rate", 
        xaxis_title = "Years", 
        yaxis_title = "Difference in percentage point"
    )

    return fig

def plot_int_rate_and_growth_rate(int_rate,growth_rate):
    fig = go.Figure()

    fig.add_trace(
        go.Line(
            x = int_rate["original_period"],
            y = int_rate["original_value"], 
            line = dict(color = "orange"), 
            name = "Long term government bond yields"
        )
    )

    fig.add_trace(
        go.Line(
            x = growth_rate["original_period"], 
            y = growth_rate["original_value"], 
            line = dict(color = "limegreen"), 
            name = "Economics Growth rate"
        )
    )
    fig.update_layout(
        xaxis_title = "Years",
        yaxis_title = "Rates (%)",
        title = "Comparison of Long Term Government Bond Yields and Economic Growth Rate",
        height = 650
    )

    return fig 