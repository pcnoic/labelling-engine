from google.cloud import storage

# Returns storage client using ENV credentials
def bucket_getClient():
    storage_client = storage.Client()
    return storage_client
