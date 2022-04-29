import main
from flask import Flask

def test_base_route():
    client = main.app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hello, world!'
    assert response.status_code == 200

def test_cow_route():
    client = main.app.test_client()
    url = '/cow'

    response = client.get(url)
    assert response.get_data() == b'MOoooOo!'
    assert response.status_code == 200
