from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

# In-memory data store
data_store = []

# GET endpoint - config fetch
@app.route('/get-config', methods=['GET'])
def get_config():
    config = {
        "fan": "off",
        "threshold": 30
    }
    return jsonify(config)

# POST endpoint - receive data
@app.route('/send-data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        if data is None:
            return "Invalid JSON!", 400

        print("Received from Raspberry Pi:", data)

        data_store.append({
            "temperature": data.get("temperature"),
            "humidity": data.get("humidity")
        })

        return "Data received!", 200

    except Exception as e:
        print("Error in /send-data:", str(e))
        return "Internal server error", 500

# NEW: GET endpoint - view stored data
@app.route('/get-data', methods=['GET'])
def get_data():
    return jsonify(data_store)
@app.route('/clear-data', methods=['GET'])
def clear_data():
    data_store.clear()
    return "Data store cleared!", 200

# Start app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
