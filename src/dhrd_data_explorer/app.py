import streamlit as st

home_page = st.Page("pages/DHRD_Corpus_Explorer.py", title="Home")
region_page = st.Page("pages/1_DHRs By Region.py", title="DHRs By Region")
incidents_page = st.Page("pages/2_Case Characteristics.py", title="Case Characteristics")
victims_page = st.Page("pages/3_Victim Demographics.py", title="Victim Demographics")
perpetrator_page = st.Page("pages/4_Perpetrator Demographics.py", title="Perpetrator Demographics")

pg = st.navigation([home_page, region_page, incidents_page, victims_page, perpetrator_page])  # about_page NOT listed here
pg.run()
