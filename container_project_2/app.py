import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import shap
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Intro Page
def intro_page():
    st.title("Machine Learning Streamlit App")
    st.write("This app demonstrates loading datasets, training a model, visualizing data, and using SHAP values.")

# Data Loading Page
def data_loading_page():
    st.title("Data Loading")
    data_file = st.file_uploader("Upload your CSV file", type=['csv'])

    if data_file is not None:
        df = pd.read_csv(data_file)
        st.write("Dataset Preview:")
        st.write(df.head())
        st.session_state['df'] = df

# Model Training Page
def model_training_page():
    st.title("Model Training")

    df = st.session_state.get('df', None)

    if df is None:
        st.warning("Please upload data first from the 'Data Loading' page.")
        return

    # Select target column
    target_column = st.selectbox("Select target column", df.columns)
    features = df.drop(columns=[target_column])
    target = df[target_column]

    # Identify numeric and categorical columns
    numeric_cols = features.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = features.select_dtypes(include=['object', 'category']).columns

    # Handle missing values
    if features.isnull().sum().sum() > 0:
        st.warning("Missing values detected. Filling with placeholder values (0 for numeric, 'missing' for categorical).")
        features[numeric_cols] = features[numeric_cols].fillna(0)
        features[categorical_cols] = features[categorical_cols].fillna('missing')

    # Preprocessing pipeline for features
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', 'passthrough', numeric_cols),
            ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_cols)
        ])

    # Create a pipeline with preprocessing and model
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    # Handle target variable (if categorical, encode it)
    if target.dtype == 'object' or target.dtype.name == 'category':
        le = LabelEncoder()
        target_encoded = le.fit_transform(target)
        st.session_state['label_encoder'] = le  # Save for later use if needed
    else:
        target_encoded = target

    # Split the data
    try:
        X_train, X_test, y_train, y_test = train_test_split(features, target_encoded, test_size=0.2, random_state=42)
    except Exception as e:
        st.error(f"Error splitting data: {str(e)}")
        return

    # Train the model
    try:
        model_pipeline.fit(X_train, y_train)
        st.write("Model trained successfully!")
    except Exception as e:
        st.error(f"Error training model: {str(e)}")
        return

    # Save the model and data
    joblib.dump(model_pipeline, 'model.pkl')
    st.session_state['model'] = model_pipeline
    st.session_state['X_test'] = X_test
    st.session_state['y_test'] = y_test
    st.session_state['feature_names'] = features.columns  # Save for SHAP

# Visualization Page
def visualization_page():
    st.title("Data Visualization")

    df = st.session_state.get('df', None)

    if df is not None:
        st.write("Select a feature to visualize:")
        feature = st.selectbox("Feature", df.columns)
        plt.figure(figsize=(10, 5))
        plt.hist(df[feature], bins=30)
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        st.pyplot(plt)
    else:
        st.warning("Please upload data first from the 'Data Loading' page.")

# SHAP Values Page
def shap_values_page():
    st.title("SHAP Values")

    model_pipeline = st.session_state.get('model', None)
    X_test = st.session_state.get('X_test', None)
    feature_names = st.session_state.get('feature_names', None)

    if model_pipeline is None or X_test is None:
        st.warning("Please train the model first from the 'Model Training' page.")
        return

    # Extract the classifier from the pipeline
    model = model_pipeline.named_steps['classifier']
    # Transform X_test using the preprocessor
    preprocessor = model_pipeline.named_steps['preprocessor']
    X_test_transformed = preprocessor.transform(X_test)

    # Get feature names after one-hot encoding
    num_features = preprocessor.transformers_[0][2]
    cat_features = preprocessor.transformers_[1][1].get_feature_names_out(preprocessor.transformers_[1][2])
    all_feature_names = list(num_features) + list(cat_features)

    # Compute SHAP values
    try:
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_test_transformed)

        st.write("SHAP Summary Plot")
        plt.figure()
        shap.summary_plot(shap_values, X_test_transformed, feature_names=all_feature_names, plot_type="bar")
        st.pyplot(plt)
    except Exception as e:
        st.error(f"Error computing SHAP values: {str(e)}")

# Main function to control the app flow
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", ["Intro", "Data Loading", "Model Training", "Visualization", "SHAP Values"])

    if page == "Intro":
        intro_page()
    elif page == "Data Loading":
        data_loading_page()
    elif page == "Model Training":
        model_training_page()
    elif page == "Visualization":
        visualization_page()
    elif page == "SHAP Values":
        shap_values_page()

if __name__ == "__main__":
    main()
