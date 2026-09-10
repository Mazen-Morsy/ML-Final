
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("heart_disease_model.pkl")

st.title("❤️ Heart Disease Prediction")
st.write("Enter the patient's information below.")

# User inputs
age = st.number_input("Age", min_value=1, max_value=120, value=50)

gender = st.selectbox(
    "Gender",
    ["male", "female"]
)

resting_bp = st.number_input(
    "Resting Blood Pressure (mmHg)",
    min_value=50,
    max_value=250,
    value=120
)

cholesterol = st.number_input(
    "Cholesterol (mg/dl)",
    min_value=50,
    max_value=600,
    value=200
)

max_heart_rate = st.number_input(
    "Maximum Heart Rate",
    min_value=50,
    max_value=250,
    value=150
)

st_depression = st.number_input(
    "ST Depression",
    min_value=0.0,
    max_value=10.0,
    value=1.0
)

chest_pain = st.selectbox(
    "Chest Pain Type",
    ["typical angina", "atypical angina", "non-anginal pain", "asymptomatic"]
)

exercise_angina = st.selectbox(
    "Exercise Induced Angina",
    ["yes", "no"]
)

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Resting_BP_mmHg": [resting_bp],
        "Cholesterol_mg/dl": [cholesterol],
        "Max_Heart_Rate": [max_heart_rate],
        "ST_Depression": [st_depression],
        "Chest_Pain_Type": [chest_pain],
        "Exercise_Induced_Angina": [exercise_angina]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Heart Disease: Detected")
    else:
        st.success("✅ Heart Disease: Not Detected")
