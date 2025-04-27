import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

st.title("⚙️ Model Training")

if "df" not in st.session_state:
    st.warning("Please load data first.")
else:
    df = st.session_state["df"]

    target = st.selectbox("Select Target Variable", df.columns)

    if st.button("Train Model"):
        X = df.drop(columns=[target])
        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        st.success("Model trained successfully!")

        st.session_state["model"] = model
        st.session_state["X_test"] = X_test
        st.session_state["y_test"] = y_test
