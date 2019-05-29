import sys

import paho.mqtt.client as mqtt  # imports the mqtt client library


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

    topic = sys.argv[1]
    print("you are subscribed to " + topic)

    client.subscribe(topic, int(sys.argv[2]))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # prints received message

    print("\n Message received with \n QOS: {} \n on topic: {} \n with payload: {}".format(msg.qos, msg.topic,
                                                                                           msg.payload))


client = mqtt.Client()  # creates client instance
client.on_connect = on_connect  # tells program the on_connect callback function
client.on_message = on_message  # tells program the on_message callback function
client.connect("test.mosquitto.org", 1883, 60)

# runs with the loop_forever function.
client.loop_forever()
