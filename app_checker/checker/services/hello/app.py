#!flask/bin/python
from flask import Flask, jsonify, render_template
import os
import requests

app = Flask(__name__)

@app.route('/hello')
def hello():
    return { "status" : "UP" }'

# Verify the status of the microservice
@app.route('/health')
def health():
    return '{ "status" : "UP" }'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
