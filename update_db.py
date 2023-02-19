import firebase_admin
from firebase_admin import credentials, db
import json
import sys
import os

cred = credentials.Certificate("../smartflow-46d1a-firebase-adminsdk-e5ck1-d4f55effa8.json") # Put the certificate here
firebase_admin.initialize_app(cred, {
    'databaseURL' : os.environ.get('DB_URL') #'https://smartflow-46d1a-default-rtdb.firebaseio.com/'
})

ref = db.reference("/")

if len(sys.argv) == 2:
    with open(sys.argv[1], "r") as f:
        data = json.load(f)
    ref.update(data)
    print("Changes updated")

else:
    print("Usage: python3 update_db.py <path_to_json>")