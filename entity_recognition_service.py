from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    '''
    Simplistic entity recognition logic
    Input: text str
    Output: results json
    '''
    
    if not request.is_json:
        print('no json data is specified')
        return jsonify({'Error': 'Incorrect service input'}), 400
        
    text = request.json.get('text')
    
    if text is None:
        return jsonify({'Error': 'Service input, empty'}), 400
        
    entities = {"entities": [{"entity": "Example Entity", "type": "Example Type"}]}
    return jsonify(entities)

