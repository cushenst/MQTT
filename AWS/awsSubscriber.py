from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import ssl
import time

# topic = input("please enter a topic \n")
topic = sys.argv[1]
# payload = input("please enter a message/payload \n")
#payload = sys.argv[3]
qos = int(sys.argv[2])

def messageRec(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

host = "amazonaws.com"  #endpoint url
port = 8883
clientId = "Intern-Test"
thingID = "Intern-Test"
caPath = "AmazonRootCA1.crt"    #Path to Ca
certPath = "certificate.pem"    #Path to cert
keyPath = "private.pem"         #Path to Private Key

myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(caPath, keyPath, certPath)

myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec


myAWSIoTMQTTClient.connect()


myAWSIoTMQTTClient.subscribe(topic, qos, messageRec)

time.sleep(2)
print("waiting for messages")
while True:
    time.sleep(1)