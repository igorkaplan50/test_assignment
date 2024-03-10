from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    '''
    Simplistic sentiment analysis logic
    Input: text str 
    Output: The  sentiment analysis result
    '''
    
    if not request.is_json:
        return jsonify({'Error': 'Incorrect service input'}), 400
        
    text = request.json.get('text', None)
    
    if text is None:
        return jsonify({'Error': 'Input error, empty'}), 400
        
    if "happy" in text:
        sentiment = "positive"
    elif "sad" in text:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return jsonify({"sentiment": sentiment})

