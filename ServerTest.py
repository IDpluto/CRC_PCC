from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def receive_data():
    data = request.get_json()
    print(data)
    # process the data here
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='192.9.66.80', port=5000)