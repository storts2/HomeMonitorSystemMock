import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime, timezone
import json

TOPIC = "bblanco/home/temperature"
SENSOR_ID = "temp01"

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

    random_temp = random.uniform(18.0, 35.0)
    rounded_temp = round(random_temp, 1)
    timestamp = datetime.now(timezone.utc).isoformat()

    message = {
        "sensor_id": SENSOR_ID,
        "temperature": rounded_temp,
        "timestamp": timestamp
    }

    json_message = json.dumps(message)

    result = client.publish(
        TOPIC,
        json_message
    )

    result.wait_for_publish()

    print("Published temperature:", rounded_temp, "C")

    time.sleep(5)


client.disconnect()
client.loop_stop()