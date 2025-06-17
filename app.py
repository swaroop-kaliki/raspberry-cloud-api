from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# In-memory data store
data_store = []

@app.route('/send-data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        if not data or not isinstance(data, list):
            return "Invalid JSON format! Expected a list.", 400

        for entry in data:
            print("Received entry:", entry)
            data_store.append(entry)

        return "Data received!", 200

    except Exception as e:
        print("Error in /send-data:", str(e))
        return "Internal server error", 500

@app.route('/get-data', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('/clear-data', methods=['GET'])
def clear_data():
    data_store.clear()
    return "Data store cleared!", 200

@app.route('/get-config', methods=['GET'])
def get_config():
    return jsonify({
        "fan": "off",
        "threshold": 30
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
