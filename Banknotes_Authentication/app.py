import streamlit as st
import pickle
import numpy as np


# Load trained model
with open("decision_tree_gini.pkl", "rb") as file:
    model = pickle.load(file)


# Title
st.title("💵 Banknote Authentication")

st.write(
    "Enter the measurements of the banknote "
    "to predict whether it is Real or Fake."
)


# Input fields
variance = st.number_input("Variance")
skewness = st.number_input("Skewness")
curtosis = st.number_input("Curtosis")
entropy = st.number_input("Entropy")


# Prediction button
if st.button("Check Banknote"):

    # Arrange inputs in the same order as training data
    input_data = np.array([
        [variance, skewness, curtosis, entropy]
    ])

    # Prediction
    prediction = model.predict(input_data)

    # Display result
    if prediction[0] == 1:
        st.success("✅ The banknote is REAL.")
    else:
        st.error("❌ The banknote is FAKE.")