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
AIO_FEED_ID = "glds.bk-iot-speaker"
AIO_USERNAME = "shiroshiro14"
AIO_KEY = "aio_BZOh93rOGiBEpjCe2v1Tw4etX6F4"

def connected(client):
    print ("Ket noi thanh cong ...")
    client.subscribe ( AIO_FEED_ID )

def subscribe(client, userdata, mid, granted_qos):
    print("Subcribed successed!")

def disconnected(client):
    print("disconnecting")
    sys.exit(1)

def message(client, feed_id, payload):
    print("Receiving from: " + feed_id)
    print("Recieiving data: " + payload)
    factory.update_json(feed_id, payload)

def gateway_update(feed_id, value): 
    if feed_id == 'glds.bk-iot-speaker': 
        bk_speaker['data'] = value
        
    elif feed_id == 'glds.bk-iot-gas': 
        bk_gas['data'] = value
    
    elif feed_id == 'glds.bk-iot-relay': 
        bk_relay['data'] = value

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
    gw_speaker['data'] = random.randint(0,1023)
    value = gw_speaker['data']
    target = gw_speaker['id']
    print("cap nhat", value)
    client.publish("glds.bk-iot-speaker", str(value))
    firebase_function.update_ref(target, value)
    time.sleep(5)