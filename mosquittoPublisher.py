import paho.mqtt.publish as publish
import sys
#topic = input("please enter a topic \n")
topic = "stephen/test"
#payload = input("please enter a message/payload \n")
payload = "hello"
publish.single(sys.argv[1], payload=sys.argv[3], qos=int(sys.argv[2]), hostname="test.mosquitto.org", port=1883, keepalive=60)