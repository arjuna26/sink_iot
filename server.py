from flask import Flask, jsonify
from google.cloud import storage
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
bucket_name = "cpsc341-text"

@app.route("/api/notes")
def list_notes():
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs()
    notes = [blob.name for blob in blobs if blob.name.endswith(".txt")]
    return jsonify(notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
