import sys

from iothub_service_client import IoTHubMessaging, IoTHubMessage, IoTHubError

open_context = 0
FEEDBACK_CONTEXT = 1

endpoint_string = sys.argv[1]
endpoint = list(map(str, endpoint_string.split(";")))

url = endpoint[0]
path = endpoint[3].replace("EntityPath=", "")

user = endpoint[1].replace("SharedAccessKeyName=", "")
password = endpoint[2].replace("SharedAccessKey=", "")

connection_string = "HostName={}.azure-devices.net;SharedAccessKeyName={};SharedAccessKey={}".format(path, user,
                                                                                                     password)

device_id = sys.argv[2]


def open_complete_callback(context):
    pass


def send_complete_callback(context, messaging_result):
    pass


def iothub_messaging_sample_run():
    try:
        iothub_messaging = IoTHubMessaging(connection_string)

        iothub_messaging.open(open_complete_callback, open_context)
        while True:
            msg_txt_formatted = input("Please enter your message: \t")
            message = IoTHubMessage(bytearray(msg_txt_formatted, 'utf8'))

            iothub_messaging.send_async(device_id, message, send_complete_callback, 0)



    except IoTHubError as iothub_error:
        print("Unexpected error {0}" % iothub_error)
        return
    except KeyboardInterrupt:
        print("IoTHubMessaging sample stopped")


if __name__ == '__main__':
    print("Starting the IoT Hub Cloud Sender")
    print("    Connection string = {0}".format(connection_string))
    print("    Device ID         = {0}".format(device_id))

    iothub_messaging_sample_run()
