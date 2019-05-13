import paho.mqtt.client as mqtt
import sys
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    topic = sys.argv[1]
    #topic = "stephen/#"
    print("you are subscribed to " + topic)
    client.subscribe(topic, int(sys.argv[2]))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("\n Message received with \n QOS: {} \n on topic: {} \n with payload: {}".format(msg.qos, msg.topic, msg.payload))
    #print(msg.topic + " "+ str(msg.payload))




client = mqtt.Client("client 1")
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()