"""
Rain Prediction App
Simple Streamlit UI for Rain Tomorrow Prediction
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Rain Predictor",
    page_icon="",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background-color: #2c3e50;
        padding: 1rem;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        border-radius: 10px;
    }
    .prediction-box {
        border: 2px solid #3498db;
        padding: 1.5rem;
        text-align: center;
        margin: 1rem 0;
        border-radius: 10px;
        background-color: #f0f8ff;
    }
    .rain {
        background-color: #c6e9ff;
        border-color: #2980b9;
    }
    .no-rain {
        background-color: #fff3cd;
        border-color: #ffc107;
    }
    .stButton button {
        background-color: #3498db;
        color: white;
        width: 100%;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        border-left: 4px solid #3498db;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header"><h1>🌧️ Rain Tomorrow Predictor</h1><p>Weather-based rainfall prediction system</p></div>', unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    try:
        model = joblib.load("rain_model.pkl")
        scaler = joblib.load("rain_scaler.pkl")
        features = joblib.load("rain_features.pkl")
        le = joblib.load("rain_label_encoder.pkl")
        return model, scaler, features, le
    except:
        return None, None, None, None

# Load model and data
model, scaler, features, le = load_model()

# Sidebar
with st.sidebar:
    st.header("Weather Parameters")
    st.markdown("---")
    
    temperature = st.slider("Temperature (°C)", -10.0, 50.0, 25.0, 0.5)
    humidity = st.slider("Humidity (%)", 0, 100, 65)
    wind_speed = st.slider("Wind Speed (km/h)", 0, 100, 15)
    cloud_cover = st.slider("Cloud Cover", 0, 8, 4)
    pressure = st.number_input("Pressure (hPa)", 990, 1030, 1012)
    
    st.markdown("---")
    predict_button = st.button("Predict Rain", use_container_width=True)

# Main content
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="metric-card"><h3>Temperature</h3><p style="font-size: 24px; font-weight: bold;">{}°C</p></div>'.format(temperature), unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card"><h3>Humidity</h3><p style="font-size: 24px; font-weight: bold;">{}%</p></div>'.format(humidity), unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card"><h3>Wind Speed</h3><p style="font-size: 24px; font-weight: bold;">{} km/h</p></div>'.format(wind_speed), unsafe_allow_html=True)

# Model status
if model is None:
    st.warning("⚠️ Model not found! Please train the model first using your Python script.")
    st.info("Run: python rain_prediction.py to train and save the model")
    st.stop()

# Prediction
if predict_button:
    # Create input data
    input_data = pd.DataFrame([[temperature, humidity, wind_speed, cloud_cover, pressure]],
                              columns=["Temperature_C", "Humidity_Percent", "Wind_Speed_kmh", "Cloud_Cover", "Pressure_hPa"])
    
    # Add dummy columns for binning features
    for col in features:
        if col not in input_data.columns:
            input_data[col] = 0
    
    # Ensure correct column order
    input_data = input_data[features]
    
    # Scale and predict
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]
    
    # Display result
    col1, col2 = st.columns(2)
    
    with col1:
        if prediction == 1:
            st.markdown(f"""
            <div class="prediction-box rain">
                <h2>🌧️ RAIN TOMORROW!</h2>
                <h3>Probability: {probability[1]*100:.1f}%</h3>
                <p>Carry an umbrella with you</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="prediction-box no-rain">
                <h2>☀️ NO RAIN TOMORROW</h2>
                <h3>Probability: {probability[1]*100:.1f}%</h3>
                <p>Enjoy the weather!</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability[1]*100,
            title={"text": "Rain Probability"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#3498db"},
                "steps": [
                    {"range": [0, 30], "color": "#fff3cd"},
                    {"range": [30, 70], "color": "#ffeaa7"},
                    {"range": [70, 100], "color": "#c6e9ff"}
                ],
                "threshold": {
                    "line": {"color": "red", "width": 4},
                    "thickness": 0.75,
                    "value": 70
                }
            }
        ))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

# Data Upload Section
st.markdown("---")
st.subheader("📊 Upload Weather Data for Batch Prediction")

uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success(f"Loaded {len(df)} records")
    st.dataframe(df.head(), use_container_width=True)
    
    if st.button("Predict for All Records", use_container_width=True):
        with st.spinner("Making predictions..."):
            # Prepare data
            df_pred = df.copy()
            
            # Add dummy columns
            for col in features:
                if col not in df_pred.columns:
                    df_pred[col] = 0
            
            # Select required columns
            df_pred = df_pred[features]
            
            # Scale
            df_scaled = scaler.transform(df_pred)
            
            # Predict
            predictions = model.predict(df_scaled)
            probabilities = model.predict_proba(df_scaled)
            
            # Add results
            results = df.copy()
            results['Predicted_Rain'] = ['Yes' if p == 1 else 'No' for p in predictions]
            results['Rain_Probability'] = [f"{p[1]*100:.1f}%" for p in probabilities]
            
            # Show summary
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Records", len(results))
            with col2:
                rain_count = (predictions == 1).sum()
                st.metric("Rain Days", rain_count)
            with col3:
                st.metric("Rain Probability", f"{(rain_count/len(results)*100):.1f}%")
            
            # Show results
            st.subheader("Prediction Results")
            st.dataframe(results, use_container_width=True)
            
            # Download button
            csv = results.to_csv(index=False)
            st.download_button(
                "Download Predictions",
                csv,
                "rain_predictions.csv",
                "text/csv"
            )

# Instructions
with st.expander("📖 How to Use"):
    st.markdown("""
    **Step 1: Train the Model**  
    First run your Python script to train and save the model:
    ```bash
    python rain_prediction.py
