from flask import Flask, request, jsonify
import requests
import json
from common import set_logger

app = Flask(__name__)
# Using the centralized logger which is defined in common.py
logger = set_logger()

@app.route('/services/init', methods=['POST'])
def init():
    '''
    The initialization endpoint, used to initialize services json
    Input: None
    Output: 200-success
    '''
    
    global services
    services = load_services('services.json')
    return jsonify({'message': '200 success'})

@app.route('/service', methods=['POST'])
    
def service():
    '''
    The main services driver
    Input: {'service': name, 'text': text}
    Output: status_code, service output: json
    '''
    
    data = request.json
    service_name = data.get('service')
    text = data.get('text')
    if service_name in services:
        logger.info('Running service: %s', service_name)
        response = requests.post(services[service_name], json={"text": text})
        return jsonify(response.json()), response.status_code
    else:
        return jsonify({"error": "Service not found"}), 404

@app.route('/services', methods=['GET'])
def list_services():
    '''
    Retrieves list of defined services
    Input: None
    Output: list of services: json
    '''
    
    service_names = services.keys()
    return jsonify({'service_names': list(services.keys())})
        
@app.route('/services', methods=['POST'])
def add_service():
    '''
    Adds the service to the list of services
    Input: {'name': service_name, 'url': service_url}
    Output: status_code
    '''
    
    if not request.is_json:
        logger.error('No json data is in the request')
        return jsonify({'Error': 'Service name is missing'}), 400
    if 'url' not in request.json:
        logger.error('incorrect input, url is missing')
        return jsonify({'Error': 'Incorrect input'}), 400
    data = request.json
    
    services[data['name']] = data['url']
    return jsonify({"message": "Service added"}), 201
            
@app.route('/services', methods=['DELETE'])
def delete_service():
    '''
    delete the service from list of services
    Input: name: name of service to delete
    Output: status_code
    '''
    
    if not request.is_json:
        logger.error('No json data is in the request')
        return jsonify({'Error': 'Service name is missing'}), 400
    data = request.json
    if 'name' not in data:
        logger.error('service name not in input json')
        return jsonify({'Error': 'Service name is missing'}), 400
        
    service_name = data['name']
    removed_service = services.pop(service_name, None)
    if removed_service:
        return jsonify({}), 204
    else:
        return jsonify({"error": "Service not found"}), 404
        
def load_services(filename):
    '''
    Loads the services json from the specified file name
    Input: filename str
    Output: services dict
    '''
    
    with open(filename) as fl:
        services = json.load(fl)
    return services

def save_services(filename, services):
    '''
    Saves the services json to the file
    Input: filename str
    Output: None
    '''
    
    with open(filename, 'w') as fl:
        json.dump(services, fl, indent=2)

services = load_services('services.json')
