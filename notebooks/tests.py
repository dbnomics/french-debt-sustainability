#%%
from dbnomics import fetch_series
import pandas as pd 
import numpy as np
import plotly_express as px
import streamlit as st 
#%%
expend_data = fetch_series(
    [
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON01.FR-D976.EUROS_COURANTS.BRUT.2010.SO",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON02.FR-D976.EUROS_COURANTS.BRUT.2010.SO",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON03.FR-D976.EUROS_COURANTS.BRUT.2010.SO",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON04.FR-D976.EUROS_COURANTS.BRUT.2010.SO",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON05.FR-D976.EUROS_COURANTS.BRUT.2010.SO",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON06.FR-D976.EUROS_COURANTS.BRUT.2010.SO",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON07.FR-D976.EUROS_COURANTS.BRUT.2010.SO",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON08.FR-D976.EUROS_COURANTS.BRUT.2010.SO",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON09.FR-D976.EUROS_COURANTS.BRUT.2010.SO",
        "INSEE/CNA-2014-DEP-APU/A.CNA_DEP_APU_CONSOLIDEES.S13.SO.VALEUR_ABSOLUE.FON10.FR-D976.EUROS_COURANTS.BRUT.2010.SO",
    ]
)
#%%
expend = expend_data[
    [
        "@frequency",
        "provider_code",
        "dataset_code",
        "Nomenclature des fonctions des administrations publiques (APU)",
        "original_period",
        "value",
    ]
].rename(
    columns={
        "Nomenclature des fonctions des administrations publiques (APU)": "Categories"
    }
)

