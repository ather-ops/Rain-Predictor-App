import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Rain Predictor", page_icon="🌧️", layout="wide")

# Title
st.title("Rain Tomorrow Predictor")
st.markdown("---")

# Load saved model
@st.cache_resource
def load_model():
    model = joblib.load("rain_model.pkl")
    scaler = joblib.load("rain_scaler.pkl")
    features = joblib.load("rain_features.pkl")
    return model, scaler, features

try:
    model, scaler, features = load_model()
    st.success("Model loaded successfully!")
except:
    st.error(" Model files not found! Please run your training code first.")
    st.stop()

# Sidebar inputs
st.sidebar.header(" Weather Parameters")

temperature = st.sidebar.slider("Temperature (°C)", 0.0, 45.0, 28.0, 0.5)
humidity = st.sidebar.slider("Humidity (%)", 0, 100, 65)
wind_speed = st.sidebar.slider("Wind Speed (km/h)", 0, 50, 15)
cloud_cover = st.sidebar.select_slider("Cloud Cover (1-5)", options=[1,2,3,4,5], value=3)
pressure = st.sidebar.number_input("Pressure (hPa)", 1000, 1030, 1012)

predict_btn = st.sidebar.button(" Predict Rain", type="primary")

# Prediction
if predict_btn:
    # Create input dataframe
    input_data = pd.DataFrame([[temperature, humidity, wind_speed, cloud_cover, pressure]],
                              columns=["Temperature_C","Humidity_Percent","Wind_Speed_kmh","Cloud_Cover","Pressure_hPa"])
    
    # Add dummy columns (for binning features)
    for col in features:
        if col not in input_data.columns:
            input_data[col] = 0
    
    input_data = input_data[features]
    
    # Predict
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]
    
    # Show results
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if prediction == 1:
            st.error("**RAIN TOMORROW!**")
            st.write("Take an umbrella!")
        else:
            st.success(" **NO RAIN TOMORROW!**")
            st.write("Enjoy the weather!")
    
    with col2:
        st.metric("Rain Probability", f"{probability[1]*100:.1f}%")
    
    with col3:
        st.metric("Confidence", f"{max(probability)*100:.1f}%")
    
    # Probability gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability[1]*100,
        title={"text": "Chance of Rain"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "red"},
            "steps": [
                {"range": [0, 30], "color": "lightgreen"},
                {"range": [30, 70], "color": "yellow"},
                {"range": [70, 100], "color": "salmon"}
            ]
        }
    ))
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info(" Adjust weather parameters in the sidebar and click Predict!")

# Footer
st.markdown("---")
st.markdown("Powered by Machine Learning")
