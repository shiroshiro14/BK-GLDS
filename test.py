import random
import time
import sys
import json
import firebase_admin
from firebase_admin import db
from Adafruit_IO import MQTTClient 
from datetime import date


#SYSTEM DATE AND TIME
today = date.today()
strTextToday = today.strftime("%B %d %Y")
print(strTextToday)

cred_obj = firebase_admin.credentials.Certificate('firebase_admin_key.JSON')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://glds-42060-default-rtdb.asia-southeast1.firebasedatabase.app/'})
ref_speaker = db.reference('/-N-Wl45v3oVXQ_q0NdsA')
ref_gas = db.reference('/-N-Wl47YbSfz-gp4uca4')
ref_relay = db.reference('/-N-Wl49AQipsuIOPTjoh')

AIO_FEED_ID = "glds.bk-iot-speaker"
AIO_USERNAME = "shiroshiro14"
AIO_KEY = "aio_aMhD048trfCmWmlaag2BEav3xwTr"

speaker = open('bk-iot-speaker.JSON')
gas = open('bk-iot-gas.JSON')
relay = open('bk-iot-relay.JSON')
#temp = open('bk-iot-temp-humid.JSON')

bk_speaker = json.load(speaker)
bk_gas = json.load(gas)
bk_relay = json.load(relay)
#bk_temp = json.load(temp)

ref_speaker.set(bk_speaker)
ref_gas.set(bk_gas)
ref_relay.set(bk_relay)
#ref.push(bk_temp)

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
    update_json(feed_id, payload)

def update_json(feed_id, payload): 
    if feed_id == 'glds.bk-iot-speaker': 
        bk_speaker['data'] = payload
        ref_speaker.set(bk_speaker)
    
    elif feed_id == 'glds.bk-iot-gas': 
        bk_gas['data'] = payload
        ref_gas.set(bk_gas)

    elif feed_id == 'glds.bk-iot-relay': 
        bk_relay['data'] = payload
        ref_relay.set(bk_relay)
    #elif feed_id == 'glds.bk-iot=temp': 
    #    bk_temp['data'] = payload
    


def gateway_update(feed_id, value): 
    if feed_id == 'glds.bk-iot-speaker': 
        bk_speaker['data'] = value
        
    elif feed_id == 'glds.bk-iot-gas': 
        bk_gas['data'] = value
    
    elif feed_id == 'glds.bk-iot-relay': 
        bk_relay['data'] = value
    
    #elif feed_id == 'glds.bk-iot=temp': 
    #    bk_temp['data'] = value
    
    client.publish(feed_id,value)

client = MQTTClient (AIO_USERNAME,AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect ()
client.loop_background ()

while True :
    
    bk_speaker['data'] = random.randint(0,1023)
    value = bk_speaker['data']
    print("cap nhat", value)
    client.publish("glds.bk-iot-speaker", value)
    ref_speaker.set(bk_speaker)
    time.sleep(5)


