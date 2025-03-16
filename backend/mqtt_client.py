import paho.mqtt.client as mqtt
import json
from database import insert_sensor_data

MQTT_BROKER = "broker.hivemq.com"
MQTT_TOPIC = "scada/sensors"

def on_message(client, userdata, message):
    data = json.loads(message.payload.decode("utf-8"))
    insert_sensor_data(data["temperature"], data["pressure"], data["flow_rate"])
    print(f"Received MQTT Data: {data}")

client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, 1883)
client.subscribe(MQTT_TOPIC)

print(f"Listening for MQTT messages on topic {MQTT_TOPIC}...")
client.loop_forever()
