import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

tasks = []

def test_create_task():
    new_task_data = {
        'title': 'New task',
        'description': 'New task description'
    }
    response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
    assert response.status_code == 201
    response_json = response.json()
    assert 'message' in response_json
    assert 'id' in response_json

def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    assert response.status_code == 200
    response_json = response.json()
    assert 'tasks' in response_json
    assert 'total' in response_json

def test_update_task():
    payload = {
        'title': 'New title',
        'description': 'New description',
        'completed': True
    }
    response = requests.put(f'{BASE_URL}/tasks/1', json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert 'message' in response_json

def test_delete_task():
    response = requests.delete(f'{BASE_URL}/tasks/1')
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['message'] ==  'Tarefa excluída com sucesso!'