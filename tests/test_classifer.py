import pytest
import json
import sys
sys.path.append('../ci-flask-api')
sys.path.append('../ci-flask-api_master')
from api.main import create_app
from flask import Flask

# Fixtures
@pytest.fixture(scope='module')
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# Tests
def test_classifier_health(client):
    res = client.get('/health')
    assert "Up" in str(res.data)


def test_classifier_no_data(client):
    res = client.get('/restaurantClassifier')
    assert "No data found" in str(res.data)

def test_classifier_bad_data(client):

    res = client.get('/restaurantClassifier', json={"restaurantName": ""})
    assert "key/value not found" in str(res.data)

    res = client.get('/restaurantClassifier', json={"restaurantName": None})
    assert "key/value not found" in str(res.data)

def test_classifier_false(client):

    res = client.get('/restaurantClassifier', json={"restaurantName": "Mc Donald's"})
    assert int(json.loads(res.data)['score']) == 0.0

def test_classifier_true(client):
    res = client.get('/restaurantClassifier', json={"restaurantName": "Rathbun Steak"})
    assert int(json.loads(res.data)['score']) == 1.0
