# IoT Assignment 3

## How to install paho-mqtt

Run "py -m pip install paho-mqtt" in the project directory terminal

## Which MQTT Broker

Eclipse Mosquitto public MQTT broker

## Three Topics

- TOPIC_TEMP: "bblanco/home/temperature"
- TOPIC_HUM: "bblanco/home/humidity"
- TOPIC: "bblanco/home/comfort"

## Prefix

bblanco

## How to run the program

Instructions
- Open the 4 terminal all in the project directory
- Run the following commands in order one command per terminal
- run "py subscriber_monitor.py"
- run "py subscriber_alert.py"
- run "py publisher_temp.py"
- run publisher_hum.py"

## Comfort Rules

- if one measursment is missing then the program does not evaluate
- if both measurements are present then the program evaluates
- if the temp is above 27 and the humidity is above 75 then the comfort level is "UNCOMFORTABLE" and the reason is "Temperature and humidity above comfort zone"
- if the temp is above 27 then the comofort level is "UNCOMFORTABLE" and the reason is "Temperature above comfort limit"
- if the humidity is above 75 then the comfort level is "UNCOMFORTABLE" and the reason is Humidity above comfort limit"
- if temp is under 27 and humidity is under 75 then the comfort level is "COMFORTABLE" and the reason is "Temperature and humidity within the comfort zone"