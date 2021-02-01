import os
import pytest
from todo_app import app
from threading import Thread
from todo_app.flask_config import TrelloConfig
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

BOARD_URL = "https://api.trello.com/1/boards/"
BOARDS_URL = "https://api.trello.com/1/members/me/boards?fields=name,url"
KEY=TrelloConfig.TRELLO_API_KEY
TOKEN=TrelloConfig.TRELLO_TOKEN

@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable 
    board_id = create_trello_board()
    # os.environ['TRELLO_BOARD_ID'] = board_id
    os.environ['BOARD_ID'] = board_id

    # construct the new application
    application = app.create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False)) 
    thread.daemon = True
    thread.start()
    yield app

    # Tear Down
    thread.join(1) 
    delete_trello_board(board_id)


def create_trello_board():
    url = BOARD_URL
    new_board_name = "Test To Do List"

    query = {
    'key': KEY,
    'token': TOKEN,
    'name': new_board_name
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )

    query = {
   'key': KEY,
   'token': TOKEN
    }

    response1 = requests.request(
    "GET",
    BOARDS_URL,
    params=query
    )

    boards = response1.json()

    for board in boards:
        if board['name'] == new_board_name:
            return board['id']
        # else:
        #     return ""    

      
def delete_trello_board(board_id):
    url = BOARD_URL + board_id

    query = {
    'key': KEY,
    'token': TOKEN
    }

    response = requests.request(
    "DELETE",
    url,
    params=query
    )
    return response

@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver    


def test_task_journey(driver, test_app): 
    driver.get('http://localhost:5000/')

    # element = driver.find_element_by_name('title')
    # element.clear()
    # element.send_keys("Add test to do item")
    # element.send_keys(Keys.RETURN)

    assert driver.title == 'To-Do App'        
       