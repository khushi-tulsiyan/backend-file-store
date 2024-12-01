import os
import hashlib
from collections import Counter

def hash_file(file):
    hasher = hashlib.sha256()
    for chunk in iter(lambda: file.read(4096), b""):
        hasher.update(chunk)
    file.seek(0) 
    return hasher.hexdigest()

def add_file(file, storage_dir):
    file_path = os.path.join(storage_dir, file.filename)
    if os.path.exists(file_path):
        return {'error': 'File already exists'}
    file.save(file_path)
    return {'message': f'{file.filename} added successfully'}

def list_files(storage_dir):
    return os.listdir(storage_dir)

def delete_file(filename, storage_dir):
    file_path = os.path.join(storage_dir, filename)
    if not os.path.exists(file_path):
        return {'error': 'File not found'}
    os.remove(file_path)
    return {'message': f'{filename} removed successfully'}

def update_file(file, filename, storage_dir):
    file_path = os.path.join(storage_dir, filename)
    file.save(file_path)
    return {'message': f'{filename} updated successfully'}

def word_count(storage_dir):
    word_count = 0
    for filename in os.listdir(storage_dir):
        file_path = os.path.join(storage_dir, filename)
        with open(file_path, 'r') as f:
            word_count += len(f.read().split())
    return {'word_count': word_count}

def frequent_words(storage_dir, order='dsc', limit=10):
    counter = Counter()
    for filename in os.listdir(storage_dir):
        file_path = os.path.join(storage_dir, filename)
        with open(file_path, 'r') as f:
            counter.update(f.read().split())
    most_common = counter.most_common(limit)
    if order == 'asc':
        most_common.reverse()
    return most_common