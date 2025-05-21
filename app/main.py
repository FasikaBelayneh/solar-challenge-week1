import streamlit as st
import pandas as pd
import plotly.express as px

# Title and description
st.title("MoonLight Energy Solar Dashboard")
st.markdown("Interactive visualization of solar radiation data for Benin, Sierra Leone, and Togo.")

# Load cleaned datasets
@st.cache_data
def load_data():
    benin_df = pd.read_csv('../data/benin_clean.csv', encoding='latin1')
    sl_df = pd.read_csv('../data/sierraleone_clean.csv', encoding='latin1')
    togo_df = pd.read_csv('../data/togo_clean.csv', encoding='latin1')
    benin_df['Country'] = 'Benin'
    sl_df['Country'] = 'Sierra Leone'
    togo_df['Country'] = 'Togo'
    return pd.concat([benin_df, sl_df, togo_df], ignore_index=True)

combined_df = load_data()

# Verify data
st.write("Data Preview:")
st.write(combined_df[['Country', 'GHI', 'DNI', 'DHI']].head())

# Country selection
st.subheader("Select Countries")
countries = st.multiselect(
    "Choose countries to compare",
    options=["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)
filtered_df = combined_df[combined_df['Country'].isin(countries)]

# GHI Boxplot
st.subheader("GHI Comparison Across Countries")
if not filtered_df.empty:
    fig = px.box(filtered_df, x='Country', y='GHI', title='GHI by Country',
                 labels={'GHI': 'GHI (W/m²)', 'Country': 'Country'})
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Please select at least one country.")

# Summary Table
st.subheader("Summary Statistics")
if not filtered_df.empty:
    summary_table = filtered_df.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(2)
    st.write(summary_table)
else:
    st.write("No data to display.")