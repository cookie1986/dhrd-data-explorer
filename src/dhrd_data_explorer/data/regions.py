import requests
import io
import geopandas as gpd
import plotly.express as px
import streamlit as st

def load_regions():
    url = (
        "https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/"
        "International_Territorial_Level_1_January_2021_UK_BUC_2022/FeatureServer/0/query"
        "?where=1=1&outFields=*&f=geojson"
    )
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    gdf = gpd.read_file(io.BytesIO(response.content))
    return gdf

@st.cache_data
def plot_reports_per_region(incident_data):

    # Calculate counts per region
    region_counts = incident_data['region'].value_counts().reset_index()
    region_counts.columns = ["region","count"]

    # Load ITL1 data
    gdf = load_regions()
    name_col = "ITL121NM"
    gdf_ew = gdf[~gdf[name_col].isin(["Scotland", "Northern Ireland"])].copy()

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
    region_counts['region'] = region_counts['region'].replace(name_fixes)

    # Merge ITL1 and region count data
    merged = gdf_ew.merge(region_counts, left_on=name_col, right_on="region", how="left")
    merged["count"] = merged["count"].fillna(0)

    # Plot
    fig = px.choropleth_mapbox(
        merged,
        geojson=merged.__geo_interface__,
        locations=merged[name_col],
        featureidkey=f"properties.{name_col}",
        color="count",
        hover_name=name_col,
        hover_data={"count": True},
        mapbox_style="carto-positron",
        center={"lat": 52.3, "lon": -2.5},
        zoom=5.3,
        opacity=0.7,
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig


@st.cache_data
def plot_regions_pie_chart(incident_data):

    # Calculate counts per region
    region_counts = incident_data['region'].value_counts().reset_index()
    region_counts.columns = ["region","count"]

    fig = px.pie(
        region_counts,
        names="region",
        values="count",
        title="Region Distribution",
        hole=0
    )
    fig.update_traces(textinfo="percent+label")
    fig.update_layout(showlegend=False)

    return fig