from dotenv import load_dotenv, find_dotenv
from todo_app import app
import pytest
import requests
import os
import vcr

from todo_app.tests.test_request import MockedRequests

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version 
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests
    with test_app.test_client() as client:
        yield client

@pytest.mark.vcr
# @pytest.mark.block_network
@vcr.use_cassette('vcr_cassettes/test_index_page.yaml', record_mode='new_episodes')
def test_index_page(client):
    response = client.get("/")

    assert response.status == '200 OK'
    response_data = str(response.data)
    assert "To-Do App" in response_data

@pytest.mark.vcr
# @pytest.mark.block_network
@vcr.use_cassette('vcr_cassettes/test_move_to_in_prgress.yaml', record_mode='new_episodes')
def test_move_to_in_prgress(client): 
    TODO_ITEM_ID=os.environ.get('TODO_ITEM_ID')   
    response = client.get('/in_progress/' + TODO_ITEM_ID)

    assert response.status == '302 FOUND'


@pytest.mark.vcr
# @pytest.mark.block_network
@vcr.use_cassette('vcr_cassettes/test_move_back_to_not_started.yaml', record_mode='new_episodes')
def test_move_back_to_not_started(client):  
    COMPLETED_ITEM_ID=os.environ.get('COMPLETED_ITEM_ID')
    response = client.get("/not_started/" + COMPLETED_ITEM_ID)

    assert response.status == '302 FOUND'

@pytest.mark.vcr
# @pytest.mark.block_network
@vcr.use_cassette('vcr_cassettes/test_move_to_completed.yaml', record_mode='new_episodes')
def test_move_to_completed(client):   
    IN_PROGRESS_ITEM_ID=os.environ.get('IN_PROGRESS_ITEM_ID') 
    response = client.get("/complete/" + IN_PROGRESS_ITEM_ID)

    assert response.status == '302 FOUND'

@pytest.mark.vcr
# @pytest.mark.block_network
@vcr.use_cassette('vcr_cassettes/test_delete_item.yaml', record_mode='new_episodes')
def test_delete_item(client):  
    REMOVE_ITEM_ID=os.environ.get('REMOVE_ITEM_ID') 
    response = client.get("/remove/" + REMOVE_ITEM_ID)

    assert response.status == '302 FOUND'