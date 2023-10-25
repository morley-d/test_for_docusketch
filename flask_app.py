from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')

db = client['my_database']
collection = db['my_collection']


@app.route('/', methods=['GET'])
def core():
    return "Hello, world!", 200

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')

    if key and value:
        existing_data = collection.find_one({'key': key})
        if existing_data:
            return jsonify({'message': 'Key already exists'}), 400
        else:
            collection.insert_one({'key': key, 'value': value})
            return jsonify({'message': 'Data created'}), 201
    else:
        return jsonify({'message': 'Invalid data'}), 400


@app.route('/update/<key>', methods=['PUT'])
def update(key):
    data = request.get_json()
    new_value = data.get('new_value')

    if key and new_value:
        existing_data = collection.find_one({'key': key})
        if existing_data:
            collection.update_one({'key': key}, {'$set': {'value': new_value}})
            return jsonify({'message': 'Data updated'}), 200
        else:
            return jsonify({'message': 'Key not found'}), 404
    else:
        return jsonify({'message': 'Invalid data'}), 400


@app.route('/read/<key>', methods=['GET'])
def read(key):
    data = collection.find_one({'key': key})

    if data:
        return jsonify({'key': data['key'], 'value': data['value']}), 200
    else:
        return jsonify({'message': 'Key not found'}), 404


if __name__ == '__main__':
    app.run(port=5050, host="0.0.0.0")
