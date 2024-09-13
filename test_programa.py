# test_programa.py
import pytest
import json
from programa import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_register(client):
    # Define the payload
    payload = {
        "nombres": "John",
        "apellidos": "Doe",
        "fecha_nacimiento": "1990-01-01",
        "password": "password123"
    }
    
    # Make a POST request to the /register endpoint
    response = client.post('/register', data=json.dumps(payload), content_type='application/json')
    
    # Assert the status code and response data
    assert response.status_code == 200
    assert response.json == {"message": "Usuario registrado exitosamente"}

def test_get_users(client):
    # Make a GET request to the /users endpoint
    response = client.get('/users')
    
    # Assert the status code and check if the response is a list
    assert response.status_code == 200
    assert isinstance(response.json, list)
