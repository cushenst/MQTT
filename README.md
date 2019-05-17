# MQTT Sample Script
##### A simple MQTT client using python for Mosquitto and AWS and Azure
# Installation
##### Using pip3
```bash
pip3 install -r requirements.txt
```

# Usage
##### To subscribe to everything please use # (eg. stephen/#)
## Mosquitto

#### Subscriber
```bash
python3 mosquittoSubscriber.py $TOPIC $QOS
```

#### Publisher
```bash
python3 mosquittoPublisher.py $TOPIC $QOS $PAYLOAD
```


## AWS


#### Subscriber
```bash
python3 awsSubscriber.py $CA_PATH $CERT_PATH $PRIVATEKEY_PATH $ENDPOINT $TOPIC $QOS
```

#### Publisher
```bash
python3 awsPublisher.py $CA_PATH $CERT_PATH $PRIVATEKEY_PATH $ENDPOINT $TOPIC $QOS $PAYLOAD
```
 
## Azure

#### Device

##### Sender
```bash
python3 azureDeviceSender.py $CERT_PATH $PRIVATEKEY_PATH $ENDPOINT $DEVICE_ID $TOPIC

``` 
##### Receiver
```bash
python3 azureDeviceReceiver.py $CERT_PATH $PRIVATEKEY_PATH $ENDPOINT $DEVICE_ID

```

#### Cloud

##### Sender
```bash
python3 azureCloudSender.py $ENDPOINT_STRING $DEVICE_ID
```

##### Receiver
```bash
python3 azureCloudReceiver.py $ENDPOINT_STRING $NUMBER_OF_PARTITION $DEVICE_ID (optional)
```