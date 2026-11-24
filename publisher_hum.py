import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime, timezone
import json

TOPIC = "bblanco/home/humidity"
SENSOR_ID = "hum01"

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.connect(
    "test.mosquitto.org",
    1883,
    60
)

client.loop_start()

for i in range(10):

    random_hum = random.randint(35, 90)
    timestamp = datetime.now(timezone.utc).isoformat()

    message = {
        "sensor_id": SENSOR_ID,
        "humidity": random_hum,
        "timestamp": timestamp
    }

    json_message = json.dumps(message)

    result = client.publish(
        TOPIC,
        json_message
    )

    result.wait_for_publish()

    print("Published temperature:", random_hum, "%")

    time.sleep(5)


client.disconnect()
client.loop_stop()