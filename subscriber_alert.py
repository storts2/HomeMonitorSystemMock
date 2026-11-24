import paho.mqtt.client as mqtt
import json
from pathlib import Path

TOPIC = "bblanco/home/comfort"
BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR/ "logs.txt"

def on_connect(client, userdata, flags, reason_code, properties):

    print("Connected with result code:", reason_code)

    client.subscribe(TOPIC)

    print("Subscribed to:", TOPIC)

def on_message(client, userdata, msg):

    data = json.loads(msg.payload.decode())

    if (data["status"] == "COMFORTABLE"):
        print("Home Comfort Status: Normal")
        print("Temperature: ", data["temperature"], "C")
        print("Humidity: ", data["humidity"], "%")
    elif (data["status"] == "UNCOMFORTABLE"):
        print("WARNING: HOME CONDITIONS ARE UNCOMFORTABLE")
        print("Temperature: ", data["temperature"], "C")
        print("Humidity: ", data["humidity"], "%")
        print("Reason: ", data["reason"], "%")

    append_data = f"{data["timestamp"]} | Temp={data["temperature"]}C | Humidity={data["humidity"]}% | {data["status"]} | {data["reason"]}\n"

    with open(LOG_FILE, "a") as file:
        file.write(append_data)

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

client.connect(
    "test.mosquitto.org",
    1883,
    60
)

print("Subscriber is running...")

client.loop_forever()