import streamlit as st

st.set_page_config(
    page_title="DHRD Corpus Explorer",
    layout='centered',
    menu_items={
    "Get Help":"mailto:darren.cook@citystgeorges.ac.uk"
    }
)

st.write("# Domestic Homicide Review Dataset (DHRD) for England and Wales - Corpus Explorer")


col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.link_button("✉️ Get Help", "mailto:darren.cook@citystgeorges.ac.uk", width="stretch")
with col2:
    st.link_button("🐞 Report a Bug", "mailto:darren.cook@citystgeorges.ac.uk?subject=Bug%20Report", width="stretch")
with col3:
    st.link_button("🐙 Source Code", "https://github.com/cookie1986/dhrd-data-explorer", width="stretch")
with col4:
    st.link_button("📥 Download", "https://zenodo.org/records/21108268", width="stretch")
with col5:
    @st.dialog("About")
    def show_about():
        st.write("The DHRD Project is....")
    if st.button("About", width="stretch"):
        show_about()

st.sidebar.success("Select an option above.")

st.markdown(
    """
    The Domestic Homicide Review Dataset (DHRD) Corpus Explorer is an 
    open-source web application built using Streamlit that allows researchers
    and policymakers the ability to explore DHRs publicly released by the UK 
    Home Office.

    
    ### How to get started...
    Select from one of the options on the left-hand sidebar to explore the dataset: 
     - DHR's by region
     - case characteristics
     - victim demographics
     - perpetrator demographics
    
    
    ### Can I download the original data files?
    Yes. The full dataset has been made freely available for those who wish to explore
    the data using other software (e.g., Excel). Click [here](https://zenodo.org/records/21108268)
    to download the raw data files. The ZIP file includes four data files (```.csv``` files),
    a codebook, README, and changelog.


    ### Limitations of usage
    The dataset is derived from publicly available Home Office metadata associated with Domestic 
    Homicide Review reports, including the tagging and filtering categories exposed through the 
    Home Office website. It is not based on manual coding of the full report texts. As a result, 
    the dataset is limited by the scope, consistency, and accuracy of the Home Office tagging 
    system.

    Some variables may be missing, unknown, inconsistently tagged, or not applicable across cases. 
    For tagged characteristics, the dataset records whether a feature was indicated by the Home 
    Office metadata; absence of a recorded feature should not necessarily be interpreted as 
    evidence that the feature was absent from the case or report.

    In the initial release, victim-level records are restricted to single-victim incidents to avoid 
    assigning characteristics to individual victims where the source data do not support this. 
    Multi-victim incidents are retained in the incident-level file and may be incorporated into future 
    victim-level releases following further review of the underlying reports.

    ### Citation
    Please use the below citation if you use our dataset in your work:

    ```
    Cook, D., & Cook, E. (2026). The Domestic Homicide Review Dataset (DHRD) 
    for England and Wales (1.0.0) [Data set]. Zenodo. 
    https://doi.org/10.5281/zenodo.21108268
    ```

    ### Contact Us
    For any queries or feedback regarding this project, please contact one of the researchers:
    - [Dr Darren Cook](mailto:darren.cook@citystgeorges.ac.uk)
    - [Dr Elizabeth Cook](mailto:elizabeth.cook@citystgeorges.ac.uk)

    
    ### Further Reading
    Please see the following resources for further information about this project:

    #### Research protocol
    ```
    Cook, D., Cook, E. A., Roy, S., Thiara, R., & Selvarajah, R. (2026). A collaborative 
    approach to applying Natural Language Processing (NLP) to Domestic Homicide Reviews 
    (DHRs): A study protocol. PLoS One, 21(5), e0348948.
    ```
"""
)