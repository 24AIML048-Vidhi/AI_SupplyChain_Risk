import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Supply Chain Risk Dashboard",
    layout="wide"
)

# Title
st.title("AI-Driven Supply Chain Risk Classification Dashboard")

st.write(
    "This dashboard visualizes supply chain operational risks "
    "using machine learning analytics."
)

# Load dataset
df = pd.read_csv(
    'data/processed_data/featured_supply_chain.csv'
)

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Risk Classification Distribution
st.subheader("Risk Classification Distribution")

risk_counts = df[
    'generated_risk_classification'
].value_counts()

st.bar_chart(risk_counts)

# Severity Level Distribution
st.subheader("Severity Level Distribution")

severity_counts = df[
    'severity_level'
].value_counts()

st.bar_chart(severity_counts)

# Risk Score Statistics
st.subheader("Risk Score Statistics")

st.write(df['risk_score'].describe())

# Correlation Matrix
st.subheader("Correlation Matrix")

correlation = df.select_dtypes(
    include=['float64', 'int64']
).corr()

st.dataframe(correlation)