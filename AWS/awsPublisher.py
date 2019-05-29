import sys
import time
import uuid

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

topic = sys.argv[5]
payload = sys.argv[7]
qos = int(sys.argv[6])

host = sys.argv[4]  # enter host endpoint
port = 8883

client_id = str(uuid.uuid4())
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
time.sleep(2)

messageJson = '{"message": "' + payload + '"}'

aws_iot_client.publish(topic, messageJson, qos)

aws_iot_client.disconnect()
