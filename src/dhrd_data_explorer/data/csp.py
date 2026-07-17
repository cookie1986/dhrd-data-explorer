import streamlit as st
import plotly.express as px

@st.cache_data
def plot_csp_pie_chart(incident_data, selected_region):

    # Standardise names to prevent mismatches
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

    incident_data['region'] = incident_data['region'].replace(name_fixes)

    # Filter incident data on selected_region
    filtered_incident_data = incident_data[incident_data['region']==selected_region]

    # Calculate counts per CSP
    csp_counts = filtered_incident_data['csp'].value_counts().reset_index()
    csp_counts.columns = ["csp","count"]

    fig = px.pie(
        csp_counts,
        names="csp",
        values="count",
        title="Community Service Partnerships Distribution",
        hole=0
    )
    fig.update_traces(textinfo="percent+label")
    fig.update_layout(showlegend=False)

    return fig