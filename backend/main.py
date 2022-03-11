from flask import Flask,jsonify,request
import os
import json

app = Flask(__name__)

@app.route('/items', methods=['GET', 'POST'])
def items():

    if request.method == 'POST':
        with open("data/items.json", "r+") as file:

            data = json.load(file)
            #request_data = request.get_json()
            
            request_data = request.data.decode('UTF-8')
            entry = {}
            entry['value'] = request_data
            data.append(entry)
            file.seek(0)
            json.dump(data, file)
    if request.method == 'GET':
        read_json()

    return jsonify(read_json())

def read_json():
    with open("data/items.json", "r") as items_file:
            itemsdata = json.load(items_file)
    return itemsdata
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)