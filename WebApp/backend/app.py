from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
Models = {
    'NaiveBayes': {
        'model': joblib.load('backend/ModelNB.joblib'),
        'vectorizer': joblib.load('backend/tf-idfNB.joblib')
    },

    

}


@app.route('/api/classify', methods=['POST'])
def classify():
    data = request.get_json()
    code = data.get('code', '')
    model_name = data.get('model', '')
    
    if not code:
        return jsonify({'error': 'No code provided'}), 400
    try:
        model_entry = Models[model_name]
        vectorizer = model_entry['vectorizer']
        model = model_entry['model']
       

        if model_name == 'NaiveBayes':
            vectorizer = model_entry['vectorizer']
            code_vector = vectorizer.transform([code])
            prediction = model.predict(code_vector)[0]
            confidence = model.predict_proba(code_vector)[0][model.classes_.tolist().index(prediction)]

        elif model_name == 'BiLSTM':
            tokenizer = model_entry['vectorizer']
            label_encoder = model_entry['label_encoder']
            code_seq = tokenizer.texts_to_sequences([code])
            padded_seq = pad_sequences(code_seq, maxlen=1000)
            probabilities = model.predict(padded_seq)
            predicted_index = probabilities.argmax(axis=1)[0]
            prediction = label_encoder.inverse_transform([predicted_index])[0]
            confidence = probabilities[0][predicted_index]

        elif model_name == 'CodeBERT':
            result = model(code)[0]
            prediction = result['label']
            confidence = result['score']

    # if not code:
    #     return jsonify({'error': 'No code provided'}), 400

    # try:
        
    #     model_entry = Models[model_name]
    #     vectorizer = model_entry['vectorizer']
    #     model = model_entry['model']

    #     code_vector = vectorizer.transform([code])
    #     prediction = model.predict(code_vector)[0]

    #     # converting code into numiricall value
    #     code_vector = vectorizer.transform([code])
    #     prediction = model.predict(code_vector)[0]

    #     # Optional: simulate confidence 
    #     confidence = model.predict_proba(code_vector).max() if hasattr(model, 'predict_proba') else 0.85

    #     return jsonify({
    #         'language': prediction,
    #         'confidence': f"{confidence * 100:.2f}%"
    #     })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)