#!flask/bin/python
from flask import Flask, jsonify
import os
from kubernetes import client, config

app = Flask(__name__)

# wellcome endpoint
@app.route('/pods')
def getAllNodes():
    config.load_kube_config()
    v1 = client.CoreV1Api()

    pods = v1.list_pod_for_all_namespaces(watch=False)

    pods_list = {}
    for pod in pods.items:
        status = {
            'name': pod.metadata.name,
            'namespace': pod.metadata.namespace,
            'node': pod.spec.node_name,
            'phase': pod.status.phase
        }
        pods_list.update(status)
    return pods_list

# Verify the status of the microservice
@app.route('/health')
def health():
    return '{ "status" : "UP" }'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
