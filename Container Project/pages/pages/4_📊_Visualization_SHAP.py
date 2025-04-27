import streamlit as st
import shap
import matplotlib.pyplot as plt

st.title("📊 Visualization and SHAP Explanation")

if "model" not in st.session_state or "X_test" not in st.session_state:
    st.warning("Please train the model first.")
else:
    model = st.session_state["model"]
    X_test = st.session_state["X_test"]

    st.subheader("Feature Importance (SHAP Values)")

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)

    st.write("### SHAP Summary Plot")
    plt.figure()
    shap.summary_plot(shap_values, X_test)
    st.pyplot(plt)
