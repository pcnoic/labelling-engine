import os
from constants import CREDENTIALS_PATH_BUCKETS

def get_bucket_credentials_path():
    dirname = os.path.dirname(__file__)
    credentials_path = os.path.join(dirname, CREDENTIALS_PATH_BUCKETS)
    
    return credentials_path

# Sets Google environment credentials that can be used by all clients. 
def set_env_creds():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = get_bucket_credentials_path()
    