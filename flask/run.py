from flask import Flask, request, jsonify
from flask_cors import CORS
from model import test
import pandas as pd
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hello!!'

@app.route('/search')
def predictInput():
    test.get_charts()
    res = {}
    n=1
    for i, item in enumerate(test.search()):
        res[i+1] = item["name"]+", " +item["url"]
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

