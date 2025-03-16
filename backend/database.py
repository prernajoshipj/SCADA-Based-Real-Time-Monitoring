import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get backend directory path
DB_PATH = os.path.join(BASE_DIR, "../data/scada_data.db")  # Ensure the correct path

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        temperature REAL,
        pressure REAL,
        flow_rate REAL
    )
    """)
    
    conn.commit()
    conn.close()

def insert_sensor_data(temp, press, flow):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO sensor_data (temperature, pressure, flow_rate) VALUES (?, ?, ?)", 
                   (temp, press, flow))
    
    conn.commit()
    conn.close()

def get_latest_readings():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 1")
    data = cursor.fetchone()
    
    conn.close()
    return data

def get_historical_readings(limit=50):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT {limit}")
    data = cursor.fetchall()
    
    conn.close()
    return data

if __name__ == "__main__":
    create_database()
