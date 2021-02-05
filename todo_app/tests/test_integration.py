from dotenv import load_dotenv, find_dotenv
from todo_app import app
import pytest
import requests
import os

from todo_app.tests.test_request import MockedRequests

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version 
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client



def test_move_to_in_prgress(monkeypatch, client): 
    TODO_ITEM_ID=os.environ.get('TODO_ITEM_ID') 
    monkeypatch.setattr(requests, "request", MockedRequests.request)
    response = client.get('/in_progress/' + TODO_ITEM_ID)

    assert response.status == '302 FOUND'


def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, "request", MockedRequests.request)
    response = client.get("/")

    assert response.status == '200 OK'
    response_data = str(response.data)
    assert "To-Do App" in response_data
    assert "Add item descriptions" in response_data

def test_move_back_to_not_started(monkeypatch, client):
    COMPLETED_ITEM_ID=os.environ.get('COMPLETED_ITEM_ID')
    monkeypatch.setattr(requests, "request", MockedRequests.request)
    response = client.get("/not_started/" + COMPLETED_ITEM_ID)

    assert response.status == '302 FOUND'

def test_move_to_completed(monkeypatch, client):
    IN_PROGTESS_ITEM_ID=os.environ.get('IN_PROGTESS_ITEM_ID')
    monkeypatch.setattr(requests, "request", MockedRequests.request)
    response = client.get("/complete/" + IN_PROGTESS_ITEM_ID)

    assert response.status == '302 FOUND'

def test_delete_item(monkeypatch, client):
    REMOVE_ITEM_ID=os.environ.get('REMOVE_ITEM_ID')
    monkeypatch.setattr(requests, "request", MockedRequests.request)
    response = client.get("/remove/" + REMOVE_ITEM_ID)

    assert response.status == '302 FOUND'
      