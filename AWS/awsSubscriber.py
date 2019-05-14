import sys
import time

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

topic = sys.argv[5]
qos = int(sys.argv[6])


def message_received(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


host = sys.argv[4]  # endpoint url
port = 8883
client_id = "Intern-Test"
thing_id = "Intern-Test"
ca_path = sys.argv[1]  # path to CA
cert_path = sys.argv[2]  # path to Cert
key_path = sys.argv[3]  # path to Private Key

aws_iot_client = AWSIoTMQTTClient(client_id)
aws_iot_client.configureEndpoint(host, port)
aws_iot_client.configureCredentials(ca_path, key_path, cert_path)

aws_iot_client.configureAutoReconnectBackoffTime(1, 32, 20)
aws_iot_client.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
aws_iot_client.configureDrainingFrequency(2)  # Draining: 2 Hz
aws_iot_client.configureConnectDisconnectTimeout(10)  # 10 sec
aws_iot_client.configureMQTTOperationTimeout(5)  # 5 sec

aws_iot_client.connect()

aws_iot_client.subscribe(topic, qos, message_received)

time.sleep(2)
print("waiting for messages")
while True:
    time.sleep(1)
