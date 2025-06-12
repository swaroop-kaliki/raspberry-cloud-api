from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Received from Raspberry Pi:", data)
    return "Data received!", 200

@app.route('/get-config', methods=['GET'])
def send_config():
    config = {'sampling_interval': 10, 'mode': 'auto'}
    return jsonify(config)

if __name__ == '__main__':
    app.run()
