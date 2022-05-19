import firebase_admin
from firebase_admin import db
import json
cred_obj = firebase_admin.credentials.Certificate('firebase_admin_key.JSON')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://glds-42060-default-rtdb.asia-southeast1.firebasedatabase.app/'})
ref = db.reference("/")
with open("bk-iot-speaker.JSON","r") as f:
    file_contents = json.load(f)

ref.push(file_contents)