import pandas as pd
import streamlit as st

@st.cache_data
def region_filter(data, selected_region):    
    name_fixes = {
        "East":"East",
        "North West":"North West (England)",
        "East Midlands":"East Midlands (England)",
        "North East":"North East (England)",
        "Greater London":"London",
        "South East":"South East (England)",
        "South West":"South West (England)",
        "Yorkshire and Humber":"Yorkshire and The Humber",
        "West Midlands":"West Midlands (England)",
        "Wales":"Wales"
    }
    data['region'] = data['region'].replace(name_fixes)

    if selected_region is not None:
        return data[data['region']==selected_region].reset_index(drop=True)
    else:
        return data