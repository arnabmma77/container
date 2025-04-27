import streamlit as st
import pandas as pd

st.title("📂 Load Dataset")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")
    st.dataframe(df)
    st.session_state["df"] = df
else:
    st.warning("Please upload a dataset.")
