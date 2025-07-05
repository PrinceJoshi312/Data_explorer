# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import csv

# Page config
st.set_page_config(page_title="Data Explorer", layout="wide")
st.title("📊 Data Exploration & Visualization Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Function to auto-detect delimiter
def detect_delimiter(uploaded_file):
    sample = uploaded_file.read(2048).decode("utf-8")
    uploaded_file.seek(0)
    try:
        dialect = csv.Sniffer().sniff(sample)
        return dialect.delimiter
    except csv.Error:
        return ","  # fallback

if uploaded_file:
    delimiter = detect_delimiter(uploaded_file)
    df = pd.read_csv(uploaded_file, delimiter=delimiter)
    
    st.success(f"File uploaded successfully! (Detected delimiter: `{delimiter}`)")
    
    # Basic Overview
    st.subheader("🔍 Dataset Overview")
    st.write("Shape:", df.shape)
    st.dataframe(df.head())

    # Expanders for column info and stats
    with st.expander("📌 Column Types & Null Counts"):
        st.write(df.dtypes)
        st.write(df.isnull().sum())

    with st.expander("📈 Statistical Summary"):
        st.write(df.describe())

    # Sidebar settings
    st.sidebar.header("🔧 Visualization Settings")
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    all_cols = df.columns.tolist()

    chart_type = st.sidebar.selectbox("Choose Chart Type", ["Histogram", "Scatter", "Boxplot", "Bar (Count)", "Correlation Heatmap"])

    # Charts
    if chart_type == "Histogram":
        col = st.sidebar.selectbox("Column", numeric_cols)
        if col:
            fig = px.histogram(df, x=col)
            st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Scatter":
        x = st.sidebar.selectbox("X Axis", numeric_cols)
        y = st.sidebar.selectbox("Y Axis", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
        if x and y:
            fig = px.scatter(df, x=x, y=y)
            st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Boxplot":
        col = st.sidebar.selectbox("Numeric Column", numeric_cols)
        if col:
            fig = px.box(df, y=col)
            st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Bar (Count)":
        col = st.sidebar.selectbox("Categorical Column", all_cols)
        if col:
            fig = px.bar(df[col].value_counts().reset_index(), x="index", y=col,
                         labels={"index": col, col: "Count"})
            st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Correlation Heatmap":
        if len(numeric_cols) >= 2:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
        else:
            st.warning("Not enough numeric columns for a correlation heatmap.")
else:
    st.info("Please upload a CSV file to begin.")
