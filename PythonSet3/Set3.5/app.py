# server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return open(r'C:\Users\Gandhi Uday\OneDrive\Desktop\Uday Works\Sem 4 material\Sem 4 Works\PPFD Lab Manual\PythonSet3\Set3.5\templates\index.html').read()

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.get_json()
    user_input = data.get('userInput', '')

    # Process the user input (For demonstration, just echoing back)
    processed_input = f"You entered: {user_input}"

    return jsonify({'message': processed_input})

if __name__ == '__main__':
    app.run(debug=True)
