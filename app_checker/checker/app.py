#!flask/bin/python
from flask import Flask, jsonify, render_template
import os
import requests

app = Flask(__name__)
URLS = os.getenv('URL_SERVICES')

@app.route('/frontend')
def hello():
    #response = requests.get(URLS[1]) #simple GET req
    #print(response)
    #json_response = response.json() #response parsed in JSON
    nodes = requests.get('http://10.0.2.14/nodes') #simple GET req
    pods = requests.get('http://10.0.2.14/pods') #simple GET req
    return render_template("main.html", pods=pods, nodes=nodes)

# Verify the status of the microservice
@app.route('/health')
def health():
    return '{ "status" : "UP" }'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
