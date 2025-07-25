import os
from google.cloud import storage

def upload_file_to_gcs(event, context):
    """Triggered from Cloud Scheduler to upload data to GCS raw bucket."""
    # Set GCS bucket and filename
    bucket_name = os.environ.get("BUCKET_NAME")
    local_file_path = os.environ.get("LOCAL_FILE_PATH")
    destination_blob_name = os.environ.get("DESTINATION_BLOB_NAME")

    # Initialize GCS client
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Upload file
    blob.upload_from_filename(local_file_path)
    print(f"✅ Uploaded {local_file_path} to gs://{bucket_name}/{destination_blob_name}")

