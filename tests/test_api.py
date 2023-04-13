import requests

# Provisional endpoint for our API
ENDPOINT = "http://localhost:8000/"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
