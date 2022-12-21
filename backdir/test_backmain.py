from backdir.backmain import app
from fastapi.testclient import TestClient
import json

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Welcome ":"This is The Default Page"}

def test_masteryi():
    response = client.get(url = "/v1/champions/masteryi")
    assert response.status_code == 200
    assert response.json()["name"] == "masteryi"