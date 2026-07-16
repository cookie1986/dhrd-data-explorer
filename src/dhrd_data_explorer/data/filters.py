import pandas as pd
import streamlit as st

@st.cache_data
def region_filter(data, selected_region):
    if selected_region is not None:
        return data[data['region']==selected_region]
    else:
        return data