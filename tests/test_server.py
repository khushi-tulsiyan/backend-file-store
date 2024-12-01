import pytest
from server.app import app
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_file(client):
    data = {'file': (open('test_file.txt', 'w+'), 'test_file.txt')}
    response = client.post('/add', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert 'added successfully' in response.json['message']
    os.remove('test_file.txt')

def test_list_files(client):
    response = client.get('/list')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_remove_file(client):
    with open('test_remove.txt', 'w') as f:
        f.write("Test content")
    client.post('/add', data={'file': (open('test_remove.txt', 'rb'), 'test_remove.txt')}, content_type='multipart/form-data')
    response = client.delete('/remove/test_remove.txt')
    assert response.status_code == 200
    assert 'removed successfully' in response.json['message']
    os.remove('test_remove.txt')

def test_word_count(client):
    with open('test_wc.txt', 'w') as f:
        f.write("word word count test")
    client.post('/add', data={'file': (open('test_wc.txt', 'rb'), 'test_wc.txt')}, content_type='multipart/form-data')
    response = client.get('/wordcount')
    assert response.status_code == 200
    assert response.json['word_count'] > 0
    os.remove('test_wc.txt')
