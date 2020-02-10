#!flask/bin/python
from flask import Flask, jsonify
import os
from kubernetes import client, config

app = Flask(__name__)

# wellcome endpoint
@app.route('/nodes')
def getAllNodes():
    config.load_kube_config()
    v1 = client.CoreV1Api()

    nodes = v1.list_node(watch=False)

    node_list =  {}

    for node in nodes.items:
        status = {
            'node': node.metadata.name,
            'status': node.status.conditions[-1].status,
            'type': node.status.conditions[-1].type,
            'reason': node.status.conditions[-1].reason,
            'msg': node.status.conditions[-1].message
        }
    node_list.update(status)
    print(node_list)
    return node_list

# Verify the status of the microservice
@app.route('/health')
def health():
    return '{ "status" : "UP" }'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
