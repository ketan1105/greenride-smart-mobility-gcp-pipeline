from flask import Flask, jsonify
from google.cloud import storage
import os

app = Flask(__name__)

# Replace with your raw bucket name (dummy or placeholder)
RAW_BUCKET_NAME = "greenride-raw-bucket"

@app.route("/push", methods=["POST"])
def push_data_to_gcs():
    client = storage.Client()
    bucket = client.get_bucket(RAW_BUCKET_NAME)

    files_to_upload = {
        "trips.json": "data_simulation/output/trips.json",
        "stations.json": "data_simulation/output/stations.json"
    }

    for gcs_filename, local_path in files_to_upload.items():
        blob = bucket.blob(f"raw/{gcs_filename}")
        blob.upload_from_filename(local_path)

    return jsonify({"message": "✅ Files pushed to GCS raw bucket"}), 200

if __name__ == "__main__":
    app.run(debug=True)
