from flask import Flask, jsonify, request

app = Flask(__name__)

store_list = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My Items',
                'price': 155
            }
        ]
    }
]


# post /store/<string: name>/<string: items>
@app.route('/create-store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    data = {
        'name': request_data['name'],
        'items': request_data['items']
    }

    store_list.append(request_data)
    return jsonify({'store-list': store_list})


# get /stores
@app.route('/get-stores', methods=['GET'])
def get_stores_list():
    return jsonify({'store-list': store_list})


# get /get-store/<string:name>
@app.route('/get-store/<string:name>', methods=['GET'])
def get_store_by_name(name):
    for store in store_list:
        if store['name'] == name:
            return jsonify(store)
    return {'message': 'No Data Found'}


app.run(port=5000)
