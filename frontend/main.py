from flask import Flask,render_template,request,redirect,url_for
import os, requests
BACKEND_SERVER = os.environ['BACKEND_SERVER']
URL = "http://" + BACKEND_SERVER + "/items"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        r=requests.get(URL)
        items = r.json()
    if request.method == 'POST':
        r=requests.post(URL, data=request.form['item'])
        return redirect(url_for('index'))
    return render_template('index.html', 
    title='Test Site', 
    appName='DB App demo',
    items = items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)