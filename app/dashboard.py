import streamlit as st
import plotly.express as px
from utils import load_data, filter_by_severity, export_to_csv

# Load data
df = load_data("data/sample_threat_data.csv")

# App title
st.title("🔒 Threat Intelligence Dashboard")

# Display data
st.subheader("Raw Threat Data")
st.dataframe(df)

# Severity filter
severity = st.selectbox("Filter by Severity", ["All", "Low", "Medium", "High", "Critical"])
if severity != "All":
    filtered_df = filter_by_severity(df, severity)
else:
    filtered_df = df

st.subheader(f"Filtered Data ({severity})")
st.dataframe(filtered_df)

# Chart - Threats by Type
fig = px.histogram(filtered_df, x="Type", color="Severity", title="Threats by Type and Severity")
st.plotly_chart(fig)

# Export option
if st.button("Export Filtered Data"):
    file_path = export_to_csv(filtered_df)
    st.success(f"Data exported to {file_path}")
import streamlit as st
import plotly.express as px
from utils import load_data, filter_by_severity, export_to_csv

# Load data
df = load_data("data/sample_threat_data.csv")

# App title
st.title("🔒 Threat Intelligence Dashboard")

# Display data
st.subheader("Raw Threat Data")
st.dataframe(df)

# Severity filter
severity = st.selectbox("Filter by Severity", ["All", "Low", "Medium", "High", "Critical"])
if severity != "All":
    filtered_df = filter_by_severity(df, severity)
else:
    filtered_df = df

st.subheader(f"Filtered Data ({severity})")
st.dataframe(filtered_df)

# Chart - Threats by Type
fig = px.histogram(filtered_df, x="Type", color="Severity", title="Threats by Type and Severity")
st.plotly_chart(fig)

# Export option
if st.button("Export Filtered Data"):
    file_path = export_to_csv(filtered_df)
    st.success(f"Data exported to {file_path}")
