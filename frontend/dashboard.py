import streamlit as st
import requests
import pandas as pd
import plotly.express as px  # Use Plotly for better visualizations

# Backend API URLs
API_URL = "http://127.0.0.1:8000/latest_readings"
HISTORICAL_API_URL = "http://127.0.0.1:8000/historical_data"

# Set Page Configuration
st.set_page_config(page_title="SCADA Monitoring", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stDataFrame {
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📊 SCADA Monitoring Dashboard")

# Fetch latest sensor data
response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()

    # Display latest readings
    st.subheader("📌 Latest Sensor Readings")
    st.json(data)

    # Alert if temperature is too high
    if data["temperature"] > 75:
        st.warning(f"⚠️ High Temperature Alert! ({data['temperature']}°C)")

else:
    st.error("❌ Error fetching latest data.")

# Fetch historical sensor data
st.subheader("📜 Historical Data")
hist_response = requests.get(HISTORICAL_API_URL, params={"limit": 50})

if hist_response.status_code == 200:
    hist_data = pd.DataFrame(hist_response.json())

    if not hist_data.empty:
        # ✅ Convert timestamp column to datetime format
        hist_data["timestamp"] = pd.to_datetime(hist_data["timestamp"])

        # ✅ Display as Table
        st.write("🗂 **Historical Sensor Data Table**")
        st.dataframe(hist_data.reset_index(drop=True), height=300)

        # ✅ Improved Historical Graph with Warning Markers
        st.write("📉 **Historical Data Trends (Last 50 Readings)**")

        # Check for high temperatures
        hist_data["High Temp Warning"] = hist_data["temperature"].apply(lambda x: "Warning" if x > 75 else "Normal")

        # Create a plotly graph
        fig = px.line(hist_data, x="timestamp", y=["temperature", "pressure", "flow_rate"], 
                      labels={"timestamp": "Time", "value": "Sensor Reading"},
                      title="Sensor Data Trends")

        # Add warning markers for high temperature events
        high_temp_points = hist_data[hist_data["temperature"] > 75]
        if not high_temp_points.empty:
            fig.add_scatter(x=high_temp_points["timestamp"], y=high_temp_points["temperature"],
                            mode="markers", marker=dict(color="red", size=10, symbol="x"),
                            name="High Temp Warning ⚠️")

        # Display the graph
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("⚠️ No historical data available.")
else:
    st.error("❌ Error fetching historical data.")
