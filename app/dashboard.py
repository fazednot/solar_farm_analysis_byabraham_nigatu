
import streamlit as st
import pandas as pd
from scripts.data_processing import load_data, clean_data, preprocess_data
from scripts.visualization import plot_time_series, plot_correlation_matrix, plot_histogram

# Load and preprocess the data
df = load_data('data/processed/solar_data.csv')
df = clean_data(df)
df = preprocess_data(df)

# Streamlit app layout
st.title("Solar Farm Data Analysis Dashboard")

# Sidebar for user input
st.sidebar.header("Visualization Settings")
visualization_type = st.sidebar.selectbox("Select visualization type", ('Time Series', 'Correlation Matrix', 'Histogram'))

# Conditional rendering based on user input
if visualization_type == 'Time Series':
    column = st.sidebar.selectbox("Select column for Time Series", df.columns[1:])
    plot_time_series(df, column, f"{column} Over Time")

elif visualization_type == 'Correlation Matrix':
    columns = st.sidebar.multiselect("Select columns for Correlation Matrix", df.columns[1:])
    if columns:
        plot_correlation_matrix(df, columns)

elif visualization_type == 'Histogram':
    column = st.sidebar.selectbox("Select column for Histogram", df.columns[1:])
    plot_histogram(df, column)