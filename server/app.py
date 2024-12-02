from flask import Flask, request, jsonify
import os
from utils import add_file, list_files, delete_file, update_file, word_count, frequent_words

app = Flask(__name__)

# Set storage directory
STORAGE_DIR = "./storage"
os.makedirs(STORAGE_DIR, exist_ok=True)

@app.route('/')
def index():
    return "File Store Service is running!"


@app.route('/add', methods=['POST'])
def add():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    result = add_file(file, STORAGE_DIR)
    return jsonify(result)

@app.route('/list', methods=['GET'])
def list_all():
    files = list_files(STORAGE_DIR)
    return jsonify(files)

@app.route('/remove/<filename>', methods=['DELETE'])
def remove(filename):
    result = delete_file(filename, STORAGE_DIR)
    return jsonify(result)

@app.route('/update/<filename>', methods=['PUT'])
def update(filename):
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    result = update_file(file, filename, STORAGE_DIR)
    return jsonify(result)

@app.route('/wordcount', methods=['GET'])
def wc():
    result = word_count(STORAGE_DIR)
    return jsonify(result)

@app.route('/freq-words', methods=['GET'])
def freq_words():
    order = request.args.get('order', 'dsc')
    limit = int(request.args.get('limit', 10))
    result = frequent_words(STORAGE_DIR, order, limit)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)