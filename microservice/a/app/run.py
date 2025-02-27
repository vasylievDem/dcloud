import json
import os

import requests
from flask import Flask

app = Flask(__name__)

rs = {
    "a": "hello from a"
}


@app.route("/a")
def a():
    return rs


@app.route("/ab")
def ab():
    response = requests.get('http://b:8080/b')
    s_rs = json.loads(response.text)
    return {**rs, **s_rs}


@app.route("/abc")
def abc():
    response_b = requests.get('http://b:8080/bc')
    s_rs_bc = json.loads(response_b.text)
    return {**rs, **s_rs_bc}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('listenport', 8080))
