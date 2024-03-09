import re
from flask import Flask, request, jsonify
from common import set_logger

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    '''
    The service entry point
    Description:counts the number of words in input text
    Input: text str
    Output: number of words.
    '''
    
    if not request.is_json:
        logger.error('no json data is specified')
        return jsonify({'Error': 'Incorrect service input'}), 400
        
    text = request.json.get('text', None)
    
    if text is None:
        return jsonify({'Words_count': 0})
        
    words = re.split(r'[ \n]+', text)
    number_of_words = len(words)
    return jsonify({'Words_count': number_of_words})

logger = set_logger('words_count')
