import logging
import sys

from azure.eventhub import EventHubClient, Offset

logger = logging.getLogger("azure")

endpoint_string = sys.argv[1]
endpoint = list(map(str, endpoint_string.split(";")))

url = endpoint[0]
url = url.replace("Endpoint=sb://", "")
path = endpoint[3].replace("EntityPath=", "")
url += path
url = "amqps://" + url

user = endpoint[1].replace("SharedAccessKeyName=", "")
password = endpoint[2].replace("SharedAccessKey=", "")

url = url

consumer_group = "$default"
offset = Offset("-1")
partition = int(sys.argv[2])

last_sn = -1

client = EventHubClient(url, debug=False, username=user, password=password)
if len(sys.argv) == 4:
    device_to_monitor = sys.argv[3]
    print(device_to_monitor)
else:
    device_to_monitor = "any"
try:
    for i in range(0, partition):
        receiver = client.add_receiver(consumer_group, str(i), prefetch=100, offset=offset)
    client.run()
    while partition > 0:
        for event_data in receiver.receive(timeout=100):
            if last_sn != event_data.sequence_number and (
                    event_data.device_id.decode() == device_to_monitor or device_to_monitor == "any"):
                print("Message from Device: \t\t'{}'\nWith Message: \t\t\t'{}'".format(
                    event_data.device_id.decode(), event_data.message))
                topic = event_data.application_properties
                topic = list(topic.keys())
                if len(topic) > 0:
                    topic = topic[0].decode()
                else:
                    topic = ""
                print(f"From Topic: \t\t\t'{topic}'\n")
            last_sn = event_data.sequence_number


except KeyboardInterrupt:
    pass
finally:
    client.stop()
