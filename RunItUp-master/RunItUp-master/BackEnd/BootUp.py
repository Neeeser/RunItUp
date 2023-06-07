import firebase_admin
from firebase_admin import credentials
import json
from BackEnd.set_info import *


'''
Bootup the firebase database connection. If so desired, reload all of the default information
'''
def initialize_firebase(loadDefaults):
    # Fetch the service account key JSON file contents
    addr = 'runitup-2e0a0-firebase-adminsdk-f35xf-6653f22d12.json'

    # remove
    addr = repr(addr)[1:-1]
    cred_obj = credentials.Certificate(addr)
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL': "https://runitup-2e0a0-default-rtdb.firebaseio.com/"
    })

    root = db.reference('root')

    if loadDefaults:
        # root.set('/GoogleMaps')
        gm = db.reference('root/GoogleMaps')
        backend = db.reference('root/backend')
        load_json_info(root, 'massLocationDump.json')
        #load_json_info(backend, 'defaults.json')
        #load_json_info(gm, 'defaults.json')

    return root


def load_json_info(root, filename):
    with open(filename, "r") as file:
        file_contents = json.load(file)
    root.set(file_contents)

