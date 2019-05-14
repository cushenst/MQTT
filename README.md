# MQTT Sample Script
##### A simple MQTT client using pythong for Mosquitto and AWS

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
python3 awsSubscriber.py $CA $CERT $PRIVATEKEY $ENDPOINT $TOPIC $QOS
```

#### Publisher
```bash
python3 awsPublisher.py $CA $CERT $PRIVATEKEY $ENDPOINT $TOPIC $QOS $PAYLOAD
```
 
