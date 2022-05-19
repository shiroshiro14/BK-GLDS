import firebase_admin
import json
import valueFactory
from firebase_admin import db

factory = valueFactory.factory()
#Open JSON file 
ff_speaker = factory.speaker
ff_gas = factory.gas
ff_relay = factory.relay
ff_pressure = factory.pressure
ff_time = factory.time

bk_speaker = json.load(ff_speaker)
bk_gas = json.load(ff_gas)
bk_relay = json.load(ff_relay)
bk_pressure = json.load(ff_pressure)
bk_time = json.load(ff_time)

def run():
    global ref_speaker_data
    global ref_gas_data
    global ref_relay_data
    global ref_pressure_data
    global ref_time_data

    cred_obj = firebase_admin.credentials.Certificate('firebase_admin_key.JSON')
    default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://glds-42060-default-rtdb.asia-southeast1.firebasedatabase.app/'})

    ref_speaker = db.reference(bk_speaker['id'])
    ref_speaker_data = db.reference(bk_speaker['id'] + '/data')

    ref_gas = db.reference(bk_gas['id'])
    ref_gas_data = db.reference(bk_gas['id'] + '/data')

    ref_relay = db.reference(bk_relay['id'])
    ref_relay_data = db.reference(bk_relay['id'] + '/data')

    ref_pressure = db.reference(bk_pressure['id'])
    ref_pressure_data = db.reference(bk_pressure['id']+ '/data')

    ref_time = db.reference(bk_time['id'])
    ref_time_data = db.reference(bk_time['id'] + '/data')   

    ref_speaker.set(bk_speaker)
    ref_gas.set(bk_gas)
    ref_relay.set(bk_relay)
    ref_pressure.set(bk_pressure)
    ref_time.set(bk_time)

def update_ref(id, value):
    if id == bk_speaker['id']:
        return ref_speaker_data.set(value)
    elif id == bk_gas['id']:
        return ref_gas_data.set(value)
    elif id == bk_relay['id']:
        return ref_relay_data.set(value)
    elif id == bk_pressure['id']:
        return ref_pressure_data.set(value)         
    elif id == bk_time['id']:
        return ref_time_data.set(value)

def get_value(id):
    if id == bk_speaker['id']:
        return ref_speaker_data.get()
    elif id == bk_gas['id']:
        return ref_gas_data.get()
    elif id == bk_relay['id']:
        return ref_relay_data.get()
    elif id == bk_pressure['id']:
        return ref_pressure_data.get()         
    elif id == bk_time['id']:
        return ref_time_data.get() 