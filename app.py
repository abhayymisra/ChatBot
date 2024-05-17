from flask import Flask, request, jsonify, send_from_directory
import openai

app = Flask(__name__, static_folder='../frontend', static_url_path='/')

# Initialize the OpenAI API client
openai.api_key = 'sk-proj-8yq5xw2pGxG6Bmw8ritIT3BlbkFJfBdXtFCHdTC7EjeeuYEB'

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question', '')
    
    if not question:
        return jsonify({'response': 'Please provide a valid question.'}), 400
    
    try:
        # Generate response using OpenAI GPT
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return jsonify({'response': answer})
    except Exception as e:
        return jsonify({'response': 'An error occurred while generating the response.'}), 500

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
