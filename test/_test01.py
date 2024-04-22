# test_app.py

import os
import sys
import pytest

# Add the project directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from ..app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Provide your valid contact details.' in response.data

def test_form_submission(client):
    response = client.post('/', data={
        'first_name': 'John',
        'last_name': 'Doe',
        'contact_no': '1234567890',
        'email': 'john@example.com',
        'username': 'johndoecdx',
        'password': 'password123'
    })
    print(response.status_code)
    assert response.status_code == 200
    assert b'Form submitted successfully!' in response.data
#test_form_submission(client())