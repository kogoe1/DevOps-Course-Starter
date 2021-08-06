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


def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, "request", MockedRequests.request)
    response = client.get("/")

    assert response.status == '200 OK'
    response_data = str(response.data)
    assert "To-Do App" in response_data
    assert "Add item descriptions" in response_data

def test_move_to_in_prgress(monkeypatch, client): 
    TODO_ITEM_ID='5fb9923734e1420b507bc75e' 
    monkeypatch.setattr(requests, "request", MockedRequests.request)
    response = client.get('/in_progress/' + TODO_ITEM_ID)

    assert response.status == '302 FOUND'


def test_move_back_to_not_started(monkeypatch, client):
    COMPLETED_ITEM_ID='5fb9924c9da5330af79e095c'
    monkeypatch.setattr(requests, "request", MockedRequests.request)
    response = client.get("/not_started/" + COMPLETED_ITEM_ID)

    assert response.status == '302 FOUND'

def test_move_to_completed(monkeypatch, client):
    IN_PROGRESS_ITEM_ID='5fb9923734e1420b507bc75e'
    monkeypatch.setattr(requests, "request", MockedRequests.request)
    response = client.get("/complete/" + IN_PROGRESS_ITEM_ID)

    assert response.status == '302 FOUND'

def test_delete_item(monkeypatch, client):
    REMOVE_ITEM_ID='5fb9923734e1420b507bc75e' 
    monkeypatch.setattr(requests, "request", MockedRequests.request)
    response = client.get("/remove/" + REMOVE_ITEM_ID)

    assert response.status == '302 FOUND'
      