import sys
from Adafruit_IO import MQTTClient

def connect(client):
    print("Connected Successfully")
    client.subcribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subcribed Successfully")

def disconnect(client):
    print("Disconnected")
    sys.exit(1)

def message(client , feed_id , payload):
    print("Enter Data:" +payload)

