from dbnomics import fetch_series
import pandas as pd

"""
Parler de l'actualité ?
How to measure debt sustainability : 
- Debt 
- Debt Service
- Part des dépenses de l'Etat 
- Debt service
- Taux à long terme 
"""

#Download Debt of the general government according to the Maastricht definition
 
def download_maa_debt_percent():
    maa_debt_percent = fetch_series('INSEE/DETTE-TRIM-APU-2014/T.DETTE_MAASTRICHT.S13.F.PROPORTION.FE.POURCENT.BRUT.2014.FALSE')
    return maa_debt_percent

def download_maa_debt():
    maa_debt = fetch_series('INSEE/DETTE-TRIM-APU-2014/T.DETTE_MAASTRICHT.S13.F.VALEUR_ABSOLUE.FE.EUROS.BRUT.2014.FALSE')
    return maa_debt

#Share of expenditures
def download_expenditures_data():
    expend_data = fetch_series([
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON01.FR-D976.EUROS_COURANTS.BRUT.2010",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON02.FR-D976.EUROS_COURANTS.BRUT.2010",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON03.FR-D976.EUROS_COURANTS.BRUT.2010",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON04.FR-D976.EUROS_COURANTS.BRUT.2010",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON05.FR-D976.EUROS_COURANTS.BRUT.2010",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON06.FR-D976.EUROS_COURANTS.BRUT.2010",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON07.FR-D976.EUROS_COURANTS.BRUT.2010",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON08.FR-D976.EUROS_COURANTS.BRUT.2010",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON09.FR-D976.EUROS_COURANTS.BRUT.2010",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON10.FR-D976.EUROS_COURANTS.BRUT.2010"
    ])

    expend = expend_data[["@frequency","provider_code", "dataset_code", "Nomenclature des fonctions des administrations publiques (APU)", "original_period", "value"]].rename(
        columns=
        {"Nomenclature des fonctions des administrations publiques (APU)" : "Categories"}
    )
    
    return expend

def transform_data_expenditures(expend):
    new_expend = expend.pivot_table(values='value', index='Categories', columns='original_period')
    sum_row = new_expend.sum()
    new_expend.loc["Total"] = sum_row

    new_expend_prop = new_expend.div(sum_row, axis = 1)
    reset_expend = new_expend_prop.reset_index()
    original_expend = pd.melt(reset_expend, id_vars =["Categories"], var_name = "original_period", value_name="value")
    return original_expend
 
#Total Gvnt revenue 
def download_gov_revenue():
    gov_rev = fetch_series("Eurostat/gov_10a_main/A.MIO_EUR.S13.TR.FR")
    return gov_rev

#Total Gvnt expenditure
def download_gov_expenditure():
    gov_expend = fetch_series("Eurostat/gov_10a_main/A.MIO_EUR.S13.TE.FR")
    return gov_expend

#Long Term Interest Rate

def download_lng_rate():
    lng_rate = fetch_series([
        "Eurostat/ei_mfir_m/M.NSA.NAP.MF-LTGBY-RT.FR",
        "Eurostat/ei_mfir_m/M.NSA.NAP.MF-LTGBY-RT.EA"
        ])
    return lng_rate
    
def download_hh_data():
    hh_df = fetch_series(
        [
            "OECD/NAAG/FRA.DBTS14_S15NDI",
            "OECD/DP_LIVE/FRA.HHSAV.TOT.PC_HHDI.A"
        ]
    )
    return hh_df 

