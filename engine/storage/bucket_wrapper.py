##########################
# Bucket Storage Wrapper #
##########################


def upload_blob(storage_client, bucket_name, source_file_name, destination_blob_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

def list_bucket_blobs(storage_client, bucket_name):
    blobs = storage_client.list_blobs(bucket_name)
    
    bucket_content = []
    for blob in blobs:
        bucket_content.append(blob.name)
        
    return bucket_content
        