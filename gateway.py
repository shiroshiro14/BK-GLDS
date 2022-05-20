import random
import time
import sys
import json
import firebase_function
import valueFactory
from Adafruit_IO import MQTTClient 
from datetime import date

factory = valueFactory.factory()
#call to json instance 
gw_speaker = json.load(factory.speaker)
gw_gas = json.load(factory.gas)
gw_relay = json.load(factory.relay)
gw_pressure = json.load(factory.pressure)
gw_time = json.load(factory.time)



#System date and time 
today = date.today()
strTextToday = today.strftime("%B %d %Y")
print(strTextToday)

#Adafruit connector
AIO_FEED_ID_1 = "glds.bk-iot-gas"
AIO_FEED_ID_2 = "glds.bk-iot-relay"
AIO_FEED_ID_3 = "glds.glds-pressure-sensor"
AIO_USERNAME = "shiroshiro14"
AIO_KEY = "aio_aUYx93Bao6ABt02fPkxeNtOtzce6"

def connected(client):
    print ("Ket noi thanh cong ...")
    client.subscribe ( AIO_FEED_ID_1)
    client.subscribe ( AIO_FEED_ID_2)
    client.subscribe ( AIO_FEED_ID_3)

def subscribe(client, userdata, mid, granted_qos):
    print("Subcribed successed!")

def disconnected(client):
    print("disconnecting")
    sys.exit(1)

def message(client, feed_id, payload):
    print("Receiving from: " + feed_id)
    print("Recieiving data: " + payload)
    

def gateway_update(feed_id, value): 
    client.publish(feed_id,value)

def firebase_init():
    firebase_function.run()

firebase_init()
client = MQTTClient (AIO_USERNAME,AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect ()
client.loop_background ()


while True: 
    gw_pressure['data'] = random.randint(200,1600)
    value = gw_pressure['data']
    target = gw_pressure['id']
    print("cap nhat", value)
    client.publish("AIO_FEED_ID_3", str(value))
    firebase_function.update_ref(target, str(value))
    time.sleep(5)