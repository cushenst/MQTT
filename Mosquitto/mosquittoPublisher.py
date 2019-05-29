import sys

import paho.mqtt.publish as publish  # import publisher library

topic = sys.argv[1]  # read the topic from the command
qos = int(sys.argv[2])  # read the qos from the command
payload = sys.argv[3]  # read the payload from the command

publish.single(topic, payload=payload, qos=qos, hostname="test.mosquitto.org", port=1883, keepalive=60)
