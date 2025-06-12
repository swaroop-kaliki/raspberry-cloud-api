from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-config', methods=['GET'])
def get_config():
    config = {
        "fan": "off",
        "threshold": 30
    }
    return jsonify(config)  # ✅ This returns proper JSON

# make sure this is at the end
import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
@app.route('/send-data', methods=['POST'])
def send_data():
    data = request.get_json()
    print("Received data:", data)  # For logging on Render
    return jsonify({"message": "Data received", "data": data})
