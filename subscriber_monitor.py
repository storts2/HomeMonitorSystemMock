import paho.mqtt.client as mqtt
import json
from datetime import datetime, timezone

TOPIC_TEMP = "bblanco/home/temperature"
TOPIC_HUM = "bblanco/home/humidity"
TOPIC = "bblanco/home/comfort"

temp = None
humidity = None

def on_connect(client, userdata, flags, reason_code, properties):

    print("Connected with result code:", reason_code)

    client.subscribe(TOPIC_TEMP)
    print("Subscribed to:", TOPIC_TEMP)

    client.subscribe(TOPIC_HUM)
    print("Subscribed to:", TOPIC_HUM)

def on_message(client, userdata, msg):
    global temp, humidity
    comfortLevel = "Not evaluated yet"
    reason = "Comfort level has not been evaluated yet"

    data = json.loads(msg.payload.decode())

    if msg.topic == TOPIC_TEMP:
        temp = data["temperature"]
    elif msg.topic == TOPIC_HUM:
        humidity = data["humidity"]

    if temp != None and humidity != None:
        if temp > 27 and humidity > 75:
            comfortLevel = "UNCOMFORTABLE"
            reason = "Temperature and humidity above comfort zone"
        elif temp > 27:
            comfortLevel = "UNCOMFORTABLE"
            reason = "Temperature above comfort limit"
        elif humidity > 75:
            comfortLevel = "UNCOMFORTABLE"
            reason = "Humidity above comfort limit"
        else:
            comfortLevel = "COMFORTABLE"
            reason = "Temperature and humidity within the comfort zone"

        print("Temperature: ", temp, "C")
        print("Humidity: ", humidity, "%")
        print("Comfort Status: ", comfortLevel)
        print("Reason: ", reason)

        timestamp = datetime.now(timezone.utc).isoformat()

        message = {
            "temperature": temp,
            "humidity": humidity,
            "status": comfortLevel,
            "reason": reason,
            "timestamp": timestamp
        }

        json_message = json.dumps(message)

        result = client.publish(
            TOPIC,
            json_message
        )

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
