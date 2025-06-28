from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Diane Web UI is running."

@app.route("/status")
def status():
    return jsonify({"status": "online", "shared_memory": os.listdir('/shared_memory')})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
