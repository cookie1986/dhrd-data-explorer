import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """Data is returned un-joined."""
    return (
        pd.read_csv("dataset/01_documents.csv"),
        pd.read_csv("dataset/02_incidents.csv"),
        pd.read_csv("dataset/03_perpetrators.csv"),
        pd.read_csv("dataset/04_victims.csv")
    )
    