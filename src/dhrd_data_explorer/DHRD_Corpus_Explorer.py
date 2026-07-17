import streamlit as st

st.set_page_config(
    page_title="DHRD Corpus Explorer",
    layout='centered',
    menu_items={
    "Get Help":"mailto:darren.cook@citystgeorges.ac.uk"
    }
)

st.write("# Domestic Homicide Review Dataset (DHRD) for England and Wales - Corpus Explorer")


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.link_button("✉️ Get Help", "mailto:darren.cook@citystgeorges.ac.uk")
with col2:
    st.link_button("🐞 Report a Bug", "mailto:darren.cook@citystgeorges.ac.uk?subject=Bug%20Report")
with col3:
    st.link_button("🐙 Source Code", "https://github.com/cookie1986/dhrd-data-explorer")
with col4:
    st.link_button("📥 Download", "https://zenodo.org/records/21108268")


st.sidebar.success("Select an option above.")

st.markdown(
    """
    The Domestic Homicide Review Dataset (DHRD) Corpus Explorer is an 
    open-source web application built using Streamlit that allows researchers
    and policymakers the ability to explore DHRs publicly released by the UK 
    Home Office.

    ### How to get started...
    Select from one of the options on the left-hand to explore case characteristics,
    or data related to victims or perpetrators. 
    
    ### Want to access the complete dataset?
    - The full dataset is freely available to download as CSV files [via Zenodo](https://zenodo.org/records/21108268).

    ### What are Domestic Homicide Reviews?

    ### Limitations of usage

    ### Citation

    ### Contact Us

    ### Further Reading

"""
)