import importlib

import streamlit as st
from charts import (
    plot_chart_exp_rev,
    plot_debt,
    plot_debt_percent,
    plot_expend_revenue,
    plot_expenditures_prop,
    plot_households_data,
    plot_int_rate_and_growth_rate,
    plot_int_rate_vs_growth_rate,
    plot_lng_rate,
    plot_pie_expenditures,
)
from data_loader import (
    download_expenditures_data,
    download_gov_expenditure,
    download_gov_revenue,
    download_growth_rate,
    download_hh_data,
    download_int_rate,
    download_lng_rate,
    download_maa_debt,
    download_maa_debt_percent,
    transform_data_expenditures,
)
from dbnomics import fetch_series
from streamlit_option_menu import option_menu


def main() -> None:
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
                "Sources",
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
        st.write(
            "**What is public debt** ?\n"
            "\n"
            "Public debt is the total amount of money that a government owes to creditors, both domestic and foreign,accumulated through the issuance of bonds.\n"
            "Public debt is an major source of resources for a government to finance public spending and address budget deficit.\n"
            "\n"
            '**What does "public debt sustainability" mean** ? \n'
            "\n"
            "According to international institutions and economist, a public debt is sustainable when the debt service is ensured at all times.\n"
            "Debt service refers to the total amount of principal and interest payments that a borrower, such as a State, is required to make on its debt over a specified period.\n"
            "\n"
            "To fullfil these requirements a State needs to be both solvent and liquid.\n"
            "The question of the french debt sustainability has become a hot topic.\n"
            "To repay its debt, France has to borrow on the markets.\n"
            "Public debt cannot increase indefinitely.\n"
            "The government's creditors are beginning to doubt its ability to borrow enough to repay its old debts and finance its deficit.\n"
            "French debt has not stopped growning since the 1980s.\n"
            "Many start to fear that the debt will become unmanageable.\n"
            "One way of stabilising debt is to set the debt-to-GDP ratio.\n"
            "An other, is the reduction of deficit which can be achieved through the implementation of austerity budgetary policies.\n"
        )
        st.write(
            "**A more formal explanation**.\n"
            "The sustainability of public debt depends on its long-term trajectory.\n"
            'It depends on the gap between the interest rate (r) and the growth rate of activity (g)\n (e.g. "Long Term Interest Rate"section).\n'
            "\n"
            "With a zero primary balance:\n"
            "- The debt ratio as a percentage of GDP increases if the interest rate is higher than the growth rate (r-g>0)\n"
            "- The debt ratio as a percentage of GDP decreases if the interest rate is higher than the growth rate (r-g<0)\n"
            "\n"
            "With a primary deficit, the effect is more uncertain:\n"
            "- r-g > 0 accelerates the rise of debt ratio \n"
            "- r - g < 0 contains the rise of debt ratio \n"
        )
        st.write(
            "With data avalaible on DBnomics charts have been created to show different indicators of the french debt"
        )

    if selected == "General Government Debt":
        st.header("General Government Debt")
        tab1, tab2 = st.tabs([":bar_chart:", ":file_folder:"])
        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                df_debt = download_maa_debt()
                fig1 = plot_debt(df_debt)
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
        tab1, tab2 = st.tabs([":bar_chart:", ":file_folder:"])
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
        tab1, tab2, tab3 = st.tabs(
            ["Bar Chart :bar_chart:", "Pie Chart :bar_chart:", ":file_folder:"]
        )
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
        tab1, tab2, tab3, tab4 = st.tabs(
            [":bar_chart:", ":bar_chart:", ":bar_chart:", ":file_folder:"]
        )

        with tab1:
            df_int_rate = download_int_rate()
            df_growth_rate = download_growth_rate()

            fig9 = plot_int_rate_vs_growth_rate(df_int_rate, df_growth_rate)
            st.plotly_chart(fig9)
        with tab2:
            df_int_rate = download_int_rate()
            df_growth_rate = download_growth_rate()
            fig10 = plot_int_rate_and_growth_rate(df_int_rate, df_growth_rate)
            st.plotly_chart(fig10)
        with tab3:
            df_lng_rate = download_lng_rate()
            fig7 = plot_lng_rate(df_lng_rate)
            st.plotly_chart(fig7)
        with tab4:
            df_lng_rate = download_lng_rate()
            df_int_rate = download_int_rate()
            df_growth_rate = download_growth_rate()
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("First Interest Rate Dataset")
                st.write(df_lng_rate)
            with col2:
                st.write("Second Interest Rate Dataset")
                st.write(df_int_rate)
            with col3:
                st.write("Growth Rate Dataset")
                st.write(df_growth_rate)
    if selected == "Households":
        df_households = download_hh_data()
        st.subheader("Households")
        tab1, tab2 = st.tabs([":bar_chart:", ":file_folder:"])
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
    if selected == "Sources":
        st.subheader("**Data**")
        st.write(
            "- [Debt-GDP-Ratio](https://db.nomics.world/INSEE/DETTE-TRIM-APU-2014/T.DETTE_MAASTRICHT.S13.F.PROPORTION.FE.POURCENT.BRUT.2014.FALSE)\n"
            "- [Debt](https://db.nomics.world/INSEE/DETTE-TRIM-APU-2014/T.DETTE_MAASTRICHT.S13.F.VALEUR_ABSOLUE.FE.EUROS.BRUT.2014.FALSE)\n"
            "- [Expenditures](https://db.nomics.world/INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON01.FR-D976.EUROS_COURANTS.BRUT.2010)\n"
            "- [Government Revenue](https://db.nomics.world/Eurostat/gov_10a_main/A.MIO_EUR.S13.TR.FR)\n"
            "- [Government Total Expenditures](https://db.nomics.world/Eurostat/gov_10a_main/A.MIO_EUR.S13.TE.FR)\n"
            "- [Interest Rate](https://db.nomics.world/Eurostat/irt_lt_mcby_a/A.MCBY.FR)"
            "- [Economic growth rate](https://db.nomics.world/OECD/MEI/FRA.NAEXKP01.GYSA.A)\n"
            "- Households data: [link](https://db.nomics.world/OECD/NAAG/FRA.DBTS14_S15NDI), [link](https://db.nomics.world/OECD/DP_LIVE/FRA.HHSAV.TOT.PC_HHDI.A) "
        )

        st.markdown("---")
        st.write("[Source Code](https://github.com/dbnomics/europe-convergence)")
        st.write("[DBnomics](https://db.nomics.world")


if __name__ == "__main__":
    main()
