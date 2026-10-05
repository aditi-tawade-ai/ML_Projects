import streamlit as st
import pickle
import numpy as np


# -----------------------------
# Load trained model and scaler
# -----------------------------

with open("kmeans_model.pkl", "rb") as file:
    kmeans = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)


# -----------------------------
# Streamlit App
# -----------------------------

st.title("Customer Segmentation using K-Means")

st.write(
    "Enter the customer's Annual Income and Spending Score "
    "to predict their customer segment."
)


# -----------------------------
# User Input
# -----------------------------

income = st.number_input(
    "Annual Income (k$)",
    min_value=0.0,
    value=50.0
)

spending_score = st.number_input(
    "Spending Score (1-100)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Cluster"):

    # Create input data
    input_data = np.array([[income, spending_score]])

    # Scale input using the SAME scaler used during training
    input_scaled = scaler.transform(input_data)

    # Predict cluster
    prediction = kmeans.predict(input_scaled)

    cluster = prediction[0]

    # Display result
    st.success(f"Customer belongs to Cluster {cluster}")