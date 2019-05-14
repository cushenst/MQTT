from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import ssl
import time

# topic = input("please enter a topic \n")
topic = sys.argv[1]
# payload = input("please enter a message/payload \n")
payload = sys.argv[3]
qos = int(sys.argv[2])

<<<<<<< HEAD
host = "amazonaws.com"
=======
host = "amazonaws.com"  #enter host endpoint
>>>>>>> 80e7f3d... Added comments and updated README
port = 8883
clientId = "Intern-Test"
thingID = "Intern-Test"
caPath = "AmazonRootCA1.crt"    #path to CA
certPath = "certificate.pem"    #path to Cert
keyPath = "private.pem"         #path to Private Key

myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(caPath, keyPath, certPath)

myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec


myAWSIoTMQTTClient.connect()
time.sleep(2)

messageJson = '{"message": "' + payload + '"}'

myAWSIoTMQTTClient.publish(topic, messageJson, qos)

myAWSIoTMQTTClient.disconnect()
