import random
import time
from database import insert_sensor_data, create_database

create_database()

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(20, 80), 2),
        "pressure": round(random.uniform(50, 200), 2),
        "flow_rate": round(random.uniform(10, 100), 2)
    }

if __name__ == "__main__":
    while True:
        data = generate_sensor_data()
        print(f"Simulated Data: {data}")
        insert_sensor_data(data["temperature"], data["pressure"], data["flow_rate"])
        time.sleep(2)
