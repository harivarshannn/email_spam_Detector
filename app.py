"""
Spam/Scam Detection Web Application
Flask backend for the spam detection frontend
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pickle
from preprocessing import preprocess_pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Load model and vectorizer at startup
print("Loading model and vectorizer...")
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
print("✓ Model loaded successfully!")

@app.route('/')
def home():
    """Render the main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint for spam prediction"""
    try:
        # Get text from request
        data = request.get_json()
        text = data.get('text', '')
        
        if not text.strip():
            return jsonify({
                'error': 'Please enter some text'
            }), 400
        
        # Preprocess
        cleaned_text = preprocess_pipeline(text)
        
        # Transform to TF-IDF
        X = vectorizer.transform([cleaned_text])
        
        # Predict
        prediction = model.predict(X)[0]
        probabilities = model.predict_proba(X)[0]
        
        # Prepare response
        result = {
            'prediction': 'spam' if prediction == 1 else 'ham',
            'label': 'SPAM' if prediction == 1 else 'LEGITIMATE',
            'confidence': float(probabilities[prediction] * 100),
            'spam_probability': float(probabilities[1] * 100),
            'ham_probability': float(probabilities[0] * 100),
            'cleaned_text': cleaned_text
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
