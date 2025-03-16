# SCADA-Based Real-Time Monitoring System 🚀

This project is a real-time **SCADA-based monitoring system** that simulates industrial sensor data, processes it via FastAPI, and visualizes trends using Streamlit.

## 🛠️ Features
✅ Real-time data acquisition (Simulated IoT Sensors)  
✅ RESTful APIs using FastAPI  
✅ SQLite database for data storage  
✅ Interactive SCADA dashboard with Streamlit  
✅ Historical data visualization & alerts for high temperature  
✅ Deployed on GitHub for version control  

## 📦 Tech Stack
- **Python, FastAPI, SQLite**
- **Streamlit (for visualization)**
- **Plotly (for interactive graphs)**
- **MQTT (for real-time communication)**
- **Render (for deployment, optional)**

## 🚀 Running the Project Locally
```sh
# Clone the repository
git clone https://github.com/prernajoshipj/SCADA-Based-Real-Time-Monitoring.git
cd SCADA-Based-Real-Time-Monitoring

# Install dependencies
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt

# Run FastAPI backend
uvicorn backend.main:app --reload

# Run Streamlit dashboard
streamlit run frontend/dashboard.py
