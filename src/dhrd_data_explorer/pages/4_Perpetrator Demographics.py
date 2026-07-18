import streamlit as st
import pandas as pd
import plotly.express as px
from data.load import load_data

st.set_page_config(
    page_title="DHRD - Perpetrators",
    layout="wide"
    # page_icon=""
)

SPECIAL_COLUMN_LABELS = {
}

def get_label(col_name):
    return SPECIAL_COLUMN_LABELS.get(col_name, col_name.replace("_", " ").title())

# Load data
data = load_data(record_id='21108268')
df = data["perpetrators"]

# Sidebar filters
with st.sidebar:
    st.header("Select filters...")

    filtered_df = df.copy()

    for col in df.columns:
        label = get_label(col)
        col_data = df[col].dropna()
        unique_vals = set(col_data.unique().tolist())

        is_yes_no = unique_vals.issubset({0, 1}) or \
                    unique_vals.issubset({True, False}) or \
                    unique_vals.issubset({"Yes", "No"}) or \
                    unique_vals.issubset({"yes", "no"})

        if is_yes_no and len(unique_vals) > 0:
            choice = st.radio(label, options=["All", "Yes", "No"], horizontal=True)
            if choice != "All":
                if unique_vals.issubset({0, 1}):
                    target = 1 if choice == "Yes" else 0
                elif unique_vals.issubset({True, False}):
                    target = True if choice == "Yes" else False
                else:
                    target = choice if "Yes" in unique_vals else choice.lower()
                filtered_df = filtered_df[filtered_df[col] == target]

        elif pd.api.types.is_numeric_dtype(df[col]):
            min_val, max_val = float(df[col].min()), float(df[col].max())
            if min_val == max_val:
                continue
            selected_range = st.slider(label, min_val, max_val, (min_val, max_val))
            filtered_df = filtered_df[filtered_df[col].between(*selected_range)]

        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            min_date, max_date = df[col].min(), df[col].max()
            selected_dates = st.date_input(label, (min_date, max_date))
            if len(selected_dates) == 2:
                start, end = selected_dates
                filtered_df = filtered_df[
                    (filtered_df[col] >= pd.Timestamp(start)) &
                    (filtered_df[col] <= pd.Timestamp(end))
                ]

        else:
            options = sorted(df[col].dropna().unique().tolist())
            if len(options) <= 50:
                selected = st.multiselect(label, options, default=[])
                if selected:
                    filtered_df = filtered_df[filtered_df[col].isin(selected)]


# Main page content
st.title("Perpetrator Demographics")

st.dataframe(
    filtered_df,
    hide_index=True
)


# Chart builder
st.markdown("## Build a chart")

# Classify columns
numeric_cols = [c for c in filtered_df.columns if pd.api.types.is_numeric_dtype(filtered_df[c])]
datetime_cols = [c for c in filtered_df.columns if pd.api.types.is_datetime64_any_dtype(filtered_df[c])]
categorical_cols = [c for c in filtered_df.columns if c not in numeric_cols and c not in datetime_cols and c not in ['incident_id','perpetrator_id']]

# Define what each chart type allows for X and Y
CHART_RULES = {
    "Bar":       {"x": categorical_cols + datetime_cols + numeric_cols, "y": None, "y_required": False},
    "Pie":      {"x": categorical_cols  + numeric_cols,     "y": None, "y_required": False},
    # "Scatter":   {"x": numeric_cols + datetime_cols,     "y": numeric_cols, "y_required": True},
    # "Histogram": {"x": numeric_cols + categorical_cols,  "y": None,         "y_required": False},
    # "Box":       {"x": categorical_cols,                 "y": numeric_cols, "y_required": True},
}

chart_type = st.selectbox("Chart type", list(CHART_RULES.keys()))
rules = CHART_RULES[chart_type]

col1, col2, col3 = st.columns(3)

with col1:
    x_choices = rules["x"]
    if not x_choices:
        st.warning("No suitable columns for the X-axis with this chart type.")
        x_col = None
    else:
        x_label = st.selectbox("X-axis", [get_label(c) for c in x_choices])
        x_col = {get_label(c): c for c in x_choices}[x_label]

with col2:
    if rules["y"] is not None:
        y_choices = rules["y"]
        if not y_choices:
            st.warning("No numeric columns available for the Y-axis.")
            y_col = None
        else:
            y_label = st.selectbox("Y-axis", [get_label(c) for c in y_choices])
            y_col = {get_label(c): c for c in y_choices}[y_label]
    else:
        y_col = None
        y_label = "Count"

with col3:
    # Color is generally safe as any categorical column
    color_label = st.selectbox("Colour by (optional)", ["None"] + [get_label(c) for c in categorical_cols + numeric_cols])
    color_map = {get_label(c): c for c in categorical_cols}
    color_col = color_map.get(color_label) if color_label != "None" else None

if x_col and (y_col or not rules["y_required"]) and not filtered_df.empty:
    plot_kwargs = {"data_frame": filtered_df, "color": color_col}

    if chart_type == "Bar":
        if y_col:
            fig = px.bar(x=filtered_df[x_col], y=filtered_df[y_col], **plot_kwargs)
        else:
            group_cols = [x_col] + ([color_col] if color_col else [])
            count_df = (
                filtered_df.groupby(group_cols, dropna=False)
                .size()
                .reset_index(name="count")
            )
            fig = px.bar(
                count_df,
                x=x_col,
                y="count",
                color=color_col if color_col else None
            )
        fig.update_traces(hovertemplate="%{x}<br>Count: %{y}<extra></extra>")
        # fig = px.bar(x=filtered_df[x_col], y=filtered_df[y_col] if y_col else None, **plot_kwargs)
    elif chart_type == "Pie":
        fig = px.pie(names=filtered_df[x_col], **plot_kwargs)
        fig.update_traces(
        textinfo="label+percent",
        hovertemplate="%{label}<br>Count: %{value}<br>Percent: %{percent}<extra></extra>"
    )
    fig.update_layout(
        xaxis_title=get_label(x_col),
        yaxis_title=y_label if y_col else "Count",
    )
    st.plotly_chart(fig, use_container_width=True)
elif filtered_df.empty:
    st.info("No data matches the current filters.")
else:
    st.info("Select valid X (and Y, if required) columns to build a chart.")