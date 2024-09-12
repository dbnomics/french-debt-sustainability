import streamlit as st 
import importlib
from streamlit_option_menu import option_menu
from dbnomics import fetch_series

from charts import (
    plot_debt_percent, 
    plot_debt,  
    plot_expend_revenue, 
    plot_expenditures_prop,
    plot_pie_expenditures,
    plot_chart_exp_rev,
    plot_lng_rate,
    plot_households_data
)
from data_loader import ( 
    download_maa_debt_percent, 
    download_maa_debt, 
    download_expenditures_data, 
    download_gov_revenue, 
    download_gov_expenditure,
    transform_data_expenditures,
    download_lng_rate,
    download_hh_data,
)  

def main() ->None:
    package_dir = importlib.resources.files("french_debt_sustainability")
    st.set_page_config(
        page_title="French Debt Sustainability",
        page_icon=str(package_dir / "images/favicon.png"),
    )
    st.image(str(package_dir / "images/dbnomics.svg"), width=300)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css(str(package_dir / "assets/styles.css"))
    st.markdown(
        """
        <style>
        hr {
            height: 1px;
            border: none;
            color: #333;
            background-color: #333;
            margin-top: 3px;
            margin-bottom: 3px;
        }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=[
                "Explanations",
                "General Government Debt",
                "Revenue VS Expenditures",
                "Public Spending by Sector",
                "Long Term Interest Rate",
                "Households",
                "Sources"
            ],
            icons=[
                "book",
                "bar-chart",
                "bar-chart",
                "bar-chart",
                "bar-chart",
                "bar-chart",
                "search",
            ],
            menu_icon=":",
            default_index=0,
        )
    
    if selected == "Explanations":
        st.title(":blue[Is French public debt sustainable?]")
        st.markdown("Work in progress...")
    
    if selected == "General Government Debt":
        st.header("General Government Debt")
        tab1,tab2 = st.tabs([":bar_chart:",":file_folder:"])
        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                df_debt = download_maa_debt()
                fig1= plot_debt(df_debt)
                st.plotly_chart(fig1)
            with col2:
                df_debt_per = download_maa_debt_percent()
                fig = plot_debt_percent(df_debt_per)
                st.plotly_chart(fig)      
        with tab2:
            st.subheader("Dataset")
            st.write(df_debt)


    if selected == "Revenue VS Expenditures":
        st.header("Revenue VS Expenditures")
        df_tot_exp = download_gov_expenditure()
        df_tot_rev = download_gov_revenue()
        tab1, tab2 = st.tabs([":bar_chart:",":file_folder:"])
        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                fig3 = plot_expend_revenue(df_tot_rev, df_tot_exp)
                st.plotly_chart(fig3)
            with col2:
                fig6 = plot_chart_exp_rev(df_tot_rev, df_tot_exp)
                st.plotly_chart(fig6)
        with tab2:
            col1, col2 = st.columns(2)
            with col1: 
                st.subheader("Revenue Data")
                st.write(df_tot_rev)
            with col2:
                st.subheader("Expenditures Data")
                st.write(df_tot_exp)
    if selected == "Public Spending by Sector": 
        st.header("Public Spending by Sector")
        df_expend = download_expenditures_data()
        df_expend_prop = transform_data_expenditures(df_expend)
        tab1, tab2, tab3 = st.tabs(["Bar Chart :bar_chart:", "Pie Chart :bar_chart:", ":file_folder:"])
        with tab1:
            fig4 = plot_expenditures_prop(df_expend_prop)
            st.plotly_chart(fig4)
        with tab2:
            fig5 = plot_pie_expenditures(df_expend_prop)
            st.plotly_chart(fig5)
        with tab3: 
            st.write(df_expend)

    if selected == "Long Term Interest Rate":
        st.header("Long Term Interest Rate") 
        df_lng_rate = download_lng_rate()
        tab1, tab2 = st.tabs([":bar_chart:", ":file_folder:"])
        with tab1:
            fig7 = plot_lng_rate(df_lng_rate)
            st.plotly_chart(fig7)
        with tab2:
            st.write(df_lng_rate)

    if selected == "Households":
        df_households = download_hh_data()
        st.subheader("Households")
        tab1, tab2 = st.tabs(
            [
                ":bar_chart:",
                ":file_folder:"
            ]
        )
        with tab1: 
            fig8 = plot_households_data(df_households)
            st.plotly_chart(fig8)
        with tab2: 
            col1, col2 = st.columns(2)
            with col1:
                st.write("Debt Dataset")
                df1 = fetch_series("OECD/NAAG/FRA.DBTS14_S15NDI")
                st.write(df1)
            with col2:
                st.write("Savings Dataset")
                df2 = fetch_series("OECD/DP_LIVE/FRA.HHSAV.TOT.PC_HHDI.A")
                st.write(df2)

if __name__ == "__main__":
    main()
