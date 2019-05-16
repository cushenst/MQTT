import ssl
import sys

from paho.mqtt import client as mqtt

baltimore_cer = "baltimorecer.cer"
device_cert = sys.argv[1]
device_cert_key = sys.argv[2]

hub_name = sys.argv[3]
device_name = sys.argv[4]


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    client.subscribe("devices/" + device_name + "/messages/#")


def on_disconnect(client, userdata, rc):
    print("Disconnected with result code: " + str(rc))


def on_message(client, userdata, msg):
    print("Message received for topic \t{}\nWith message \t\t\t{}\n".format(msg.topic, msg.payload))


client = mqtt.Client(client_id=device_name, protocol=mqtt.MQTTv311)
client.on_connect = on_connect

client.on_disconnect = on_disconnect
client.on_message = on_message
client.username_pw_set(username=hub_name + "/" + device_name, password=None)

client.tls_set(ca_certs=baltimore_cer, certfile=device_cert, keyfile=device_cert_key,
               cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

client.tls_insecure_set(True)

client.connect(hub_name, port=8883)
client.loop_forever()
