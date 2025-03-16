from fastapi import FastAPI
from database import get_latest_readings, get_historical_readings

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SCADA API is running!"}

@app.get("/latest_readings")
def latest_readings():
    data = get_latest_readings()
    if data:
        return {
            "id": data[0],
            "timestamp": data[1],
            "temperature": data[2],
            "pressure": data[3],
            "flow_rate": data[4]
        }
    return {"message": "No data available"}

@app.get("/historical_data")
def historical_data(limit: int = 50):
    """Fetch last N historical sensor readings."""
    data = get_historical_readings(limit)
    return [{"id": row[0], "timestamp": row[1], "temperature": row[2], "pressure": row[3], "flow_rate": row[4]} for row in data]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
