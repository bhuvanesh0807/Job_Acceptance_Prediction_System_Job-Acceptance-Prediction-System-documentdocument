import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="HR Predictor", layout="centered")

try:
    model = joblib.load('Final_Candidate_Predictions.csv')
    st.success("✅ Model Loaded Successfully")
except:
    st.error("❌ Error: 'Final_Candidate_Predictions.csv' not found in folder!")

st.title("💼 Job Acceptance Prediction")
st.write("Fill in candidate details to see if they will accept the offer.")

ssc = st.number_input("10th Score (%)", 0, 100, 75)
hsc = st.number_input("12th Score (%)", 0, 100, 70)
degree = st.number_input("Degree Score (%)", 0, 100, 65)
tech = st.number_input("Technical Score", 0, 100, 80)
apt = st.number_input("Aptitude Score", 0, 100, 75)
exp = st.number_input("Experience (Years)", 0, 20, 1)


if st.button("Predict"):
    features = pd.DataFrame([[ssc, hsc, degree, tech, apt, exp]], columns=['ssc_percentage', 'hsc_percentage', 'degree_percentage','technical_score', 'aptitude_score', 'years_of_experience'])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.success("🎯 This candidate is likely to ACCEPT!")
    else:
        st.warning("⚠️ This candidate is likely to' REJECT.")
