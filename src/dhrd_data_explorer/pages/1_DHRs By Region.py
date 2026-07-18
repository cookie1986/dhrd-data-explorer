import streamlit as st
from datetime import date
from data.load import load_data
from data.version import get_latest_version
from data.regions import plot_reports_per_region, plot_regions_pie_chart
from data.csp import plot_csp_pie_chart
from data.filters import region_filter

st.set_page_config(
    page_title="DHRs by Region",
    layout="wide"
    # page_icon=""
)

# Load data
data = load_data(record_id='21108268')

# Current version
version = get_latest_version(record_id=21108268)

st.markdown("# DHRs by Region")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Current Version",
        value=version,
        help="The current version of the dataset.",
        border=True,
        height = 135
    )

with col2:
    st.metric(
        label="Total Reports in Dataset",
        value=len(data["documents"]),
        delta=0,
        help=f"The total number of DHR reports in the current version ({version}) of the dataset.",
        border=True,
        delta_description="Reports added since last update.",
        height = 135
    )

with col3:
    st.metric(
        label="Last Updated",
        value=str(date.today()),
        help=f"The date of the latest update.",
        border=True,
        height = 135
    )

# further down - a fresh, independent row of columns
map_col, side_col = st.columns([2, 1])

with map_col:
    fig = plot_reports_per_region(incident_data=data["incidents"])
    event = st.plotly_chart(
        fig,
        use_container_width=True,
        on_select="rerun",
        key="region_map",
    )

selected_region = None
if event and event["selection"]["points"]:
    selected_region = event["selection"]["points"][0]["location"]

if selected_region:
    st.caption("Click a region on the map to see its records.")
    st.subheader(f"Records in {selected_region}")
    st.dataframe(region_filter(data["incidents"], selected_region=selected_region))

    with side_col:
        st.plotly_chart(plot_csp_pie_chart(data['incidents'], selected_region), use_container_width=True)

else:
    st.caption("Click a region on the map to see its records.")
    st.subheader(f"All records")
    st.dataframe(region_filter(data["incidents"], selected_region=None))

    with side_col:
        st.plotly_chart(plot_regions_pie_chart(data["incidents"]), use_container_width=True)