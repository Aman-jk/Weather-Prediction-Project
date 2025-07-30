# app.py

import streamlit as st
import joblib
import numpy as np


model = joblib.load("New_weather_model.pkl")


st.set_page_config(page_title="Weather Temperature Predictor", layout="centered")

st.title("🌤️ Weather Temperature Predictor")
st.markdown("Enter the weather conditions below to predict the **Temperature (°C)**.")


humidity = st.slider("Humidity (%)", 0, 100, 50)
wind_speed = st.slider("Wind Speed (km/h)", 0, 150, 10)
pressure = st.slider("Pressure (millibars)", 870, 1085, 1013)


if st.button("Predict Temperature"):
    input_data = np.array([[humidity, wind_speed, pressure]])
    predicted_temp = model.predict(input_data)[0]
    st.success(f"🌡️ Predicted Temperature: **{predicted_temp:.2f} °C**")
