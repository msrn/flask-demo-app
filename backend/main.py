from flask import Flask,jsonify,request
import os

app = Flask(__name__)
itemList = ["one","two","three"]

@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'POST':
        itemList.append(request.data.decode('UTF-8'))
    return jsonify(itemList)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)