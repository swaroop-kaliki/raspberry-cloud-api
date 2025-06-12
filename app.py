from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# ---------------------------
# GET endpoint - config fetch
# ---------------------------
@app.route('/get-config', methods=['GET'])
def get_config():
    config = {
        "fan": "off",
        "threshold": 30
    }
    return jsonify(config)  # ✅ This ensures response is JSON


# ---------------------------
# POST endpoint - send sensor data
# ---------------------------
@app.route('/send-data', methods=['POST'])
def send_data():
    data = request.get_json()
    print("Received data:", data)  # ✅ Appears in Render logs
    return jsonify({"message": "Data received", "data": data})


# ---------------------------
# Run the app on Render
# ---------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render uses PORT env var
    app.run(host="0.0.0.0", port=port)
