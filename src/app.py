Below is the main application file for the Streamlit web dashboard:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    # Load dataset (replace 'data/sample_data.csv' with your actual data file)
    return pd.read_csv("data/sample_data.csv")

def main():
    st.title("HyCAN Catalyst Analysis Dashboard")
    
    st.sidebar.header("Navigation")
    options = st.sidebar.radio("Go to", ["Home", "Data Visualization", "Model Prediction"])

    if options == "Home":
        st.subheader("Welcome to the HyCAN Dashboard")
        st.write("Explore data, visualize insights, and predict catalyst performance.")

    elif options == "Data Visualization":
        st.subheader("Visualize Dataset")
        data = load_data()
        if st.checkbox("Show Dataset"):
            st.write(data.head())
        fig = px.scatter(data, x="Feature1", y="Feature2", color="Category")
        st.plotly_chart(fig)

    elif options == "Model Prediction":
        st.subheader("Predict Catalyst Performance")
        st.write("[Model prediction module coming soon]")

if __name__ == "__main__":
    main()
