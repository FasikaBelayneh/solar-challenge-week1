import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("MoonLight Energy Solar Dashboard")
st.markdown("Interactive visualization of solar radiation data for Benin, Sierra Leone, and Togo.")

# Define data directory
DATA_DIR = os.path.join(os.path.dirname(__file__), '../data')

@st.cache_data
def load_data():
    try:
        benin_df = pd.read_csv(os.path.join(DATA_DIR, 'benin_clean.csv'), encoding='latin1', engine='python')
        sl_df = pd.read_csv(os.path.join(DATA_DIR, 'sierraleone_clean.csv'), encoding='latin1', engine='python')
        togo_df = pd.read_csv(os.path.join(DATA_DIR, 'togo_clean.csv'), encoding='latin1', engine='python')
        benin_df['Country'] = 'Benin'
        sl_df['Country'] = 'Sierra Leone'
        togo_df['Country'] = 'Togo'
        combined_df = pd.concat([benin_df, sl_df, togo_df], ignore_index=True)
        # Ensure non-negative values (fallback)
        for col in ['GHI', 'DNI', 'DHI']:
            if (combined_df[col] < 0).any():
                st.warning(f"Negative values detected in {col}. Clipping to zero.")
                combined_df[col] = combined_df[col].clip(lower=0)
        return combined_df
    except FileNotFoundError as e:
        st.error(f"File not found: {str(e)}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame()

combined_df = load_data()

if not combined_df.empty:
    st.write("Data Preview:")
    st.write(combined_df[['Country', 'GHI', 'DNI', 'DHI']].head())

    st.subheader("Select Countries")
    countries = st.multiselect(
        "Choose countries to compare",
        options=["Benin", "Sierra Leone", "Togo"],
        default=["Benin", "Sierra Leone", "Togo"]
    )
    filtered_df = combined_df[combined_df['Country'].isin(countries)]

    st.subheader("GHI Comparison Across Countries")
    if not filtered_df.empty:
        fig = px.box(filtered_df, x='Country', y='GHI', title='GHI by Country',
                     labels={'GHI': 'GHI (W/m²)', 'Country': 'Country'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please select at least one country.")

    st.subheader("Summary Statistics")
    summary_table = filtered_df.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(2)
    st.write(summary_table)
else:
    st.error("No data loaded. Please ensure CSV files exist in the data/ directory.")