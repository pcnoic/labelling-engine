import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Using a service account for authenticating against firestore 

CREDENTIALS_PATH = '../credentials/tynr/engine/firestoreServiceAccount.json'

def get_credentials_path():
    dirname = os.path.dirname(__file__)
    credentials_path = os.path.join(dirname, CREDENTIALS_PATH)   
    
    return credentials_path 
    
def fs_getAuth():
    cred = credentials.Certificate(get_credentials_path())
    firebase_admin.initialize_app(cred)

    return firestore.client()
