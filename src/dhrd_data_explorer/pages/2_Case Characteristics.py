import streamlit as st
from data.load import load_data

st.set_page_config(
    page_title="DHRD - Incidents",
    layout="wide"
    # page_icon=""
)

# Load data
data = load_data()
data = data[1] # select incident data

# Sidebar filters
with st.sidebar:
    st.header("Select filters...")
    # add filters here...

# apply filters to dataframe

# Main page content
st.markdown("# Case Characteristics")

col1, col2 = st.columns(2)
with col1:
    st.write("Here is soem text")
with col2:
    st.write("Here is soem text")