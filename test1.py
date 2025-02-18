from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

uri = "mongodb+srv://banentremen:Pkm4TgtZ1UQwU1Fd@cluster0.wkjwq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client.banen
collection = db.temp

@app.route('/sensor1', methods=['POST'])
def sensor1():
    temperature = request.args.get('temperature', type=float)
    kelembapan = request.args.get('kelembapan', type=float)
    timestamp = request.args.get('timestamp', default=datetime.now().isoformat())

    if temperature is None or kelembapan is None:
        return jsonify(error="Missing temperature or kelembapan in request parameters"), 400

    sensor_data = {
        "temperature": temperature,
        "kelembapan": kelembapan,
        "timestamp": timestamp
    }

    result = collection.insert_one(sensor_data)

    return jsonify(message="Data received and stored", inserted_id=str(result.inserted_id)), 201

@app.route('    ', methods=['GET'])
def temperature_avg():
    temperature_data = list(collection.find({}, {"temperature": 1, "_id": 0}))

    temperatures = [entry['temperature'] for entry in temperature_data]

    if len(temperatures) > 0:
        average_temperature = sum(temperatures) / len(temperatures)
    else:
        average_temperature = 0

    return jsonify(average_temperature=round(average_temperature, 2))

@app.route('/sensor1/kelembapan/avg', methods=['GET'])
def kelembapan_avg():
    kelembapan_data = list(collection.find({}, {"kelembapan": 1, "_id": 0}))

    kelembapan_values = [entry['kelembapan'] for entry in kelembapan_data]

    if len(kelembapan_values) > 0:
        average_kelembapan = sum(kelembapan_values) / len(kelembapan_values)
    else:
        average_kelembapan = 0

    return jsonify(average_kelembapan=round(average_kelembapan, 2))

if __name__ == '__main__':
    app.run(debug=True)