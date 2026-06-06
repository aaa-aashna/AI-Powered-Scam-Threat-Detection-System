import streamlit as st
import joblib

st.title("AI Scam Threat Detector")

st.write("Enter a message to detect if it's scam/spam.")

model = joblib.load("models/model.pkl")

message = st.text_area("Message")

if st.button("Predict"):

    prediction = model.predict([message])

    if prediction[0] == 1:
        st.error("Scam/Spam Detected")
    else:
        st.success("Safe Message")