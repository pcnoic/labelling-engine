import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from constants import CREDENTIALS_PATH_FIRESTORE

# Using a service account for authenticating against firestore 

def get_fs_credentials_path():
    dirname = os.path.dirname(__file__)
    credentials_path = os.path.join(dirname, CREDENTIALS_PATH_FIRESTORE)   
    
    return credentials_path 
    
def fs_getClient():
    cred = credentials.Certificate(get_fs_credentials_path())
    firebase_admin.initialize_app(cred)

    return firestore.client()
