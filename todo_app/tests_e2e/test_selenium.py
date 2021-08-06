import os
import pytest
import requests

from todo_app import app, data
from threading import Thread

from dotenv import load_dotenv, find_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

BOARD_URL = "https://api.trello.com/1/boards/"
BOARDS_URL = "https://api.trello.com/1/members/me/boards?fields=name,url"

# file_path = find_dotenv('.env')
# load_dotenv(file_path, override=True)

# KEY=os.environ.get('TRELLO_API_KEY')
# TOKEN=os.environ.get('TRELLO_TOKEN') 

KEY=''
TOKEN='' 

@pytest.fixture(scope='module')
def test_app():

    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)

    KEY=os.environ.get('TRELLO_API_KEY')
    TOKEN=os.environ.get('TRELLO_TOKEN') 

    # Create the new board & update the board id environment variable 
    board_id = create_trello_board()

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

    KEY=os.environ.get('TRELLO_API_KEY')
    TOKEN=os.environ.get('TRELLO_TOKEN') 

    query = {
    'key': KEY,
    'token': TOKEN,
    'name': new_board_name
    }

    create_test_board_response = requests.request(
    "POST",
    url,
    params=query
    )

    query = {
   'key': KEY,
   'token': TOKEN
    }

    get_boards_response = requests.request(
    "GET",
    BOARDS_URL,
    params=query
    )

    boards = get_boards_response.json()

    for board in boards:
        if board['name'] == new_board_name:
            return board['id']   

      
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
    # with webdriver.Firefox() as driver:
    with webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options) as driver:
        yield driver    


def test_task_journey(driver, test_app): 
    driver.get('http://localhost:5000/')

    # Add a todo item
    test_item = "Add test to do item"

    todo_title = driver.find_element_by_name('title')
    todo_title.clear()
    todo_title.send_keys(test_item)
    todo_title.send_keys(Keys.RETURN)

    driver.implicitly_wait(30)


    assert driver.find_element_by_xpath('//td[contains(., "' + test_item + '")]') is not None
    
    web_page_data =  driver.page_source
    assert driver.title == 'To-Do App'
    assert "Move to In Progress" in web_page_data    
    # assert "Mark as Completed" not in web_page_data    

    # Move test item to in progress
    move_to_in_progress_button = driver.find_element_by_xpath('//a[@class="btn btn-primary"][contains(., "Move to In Progress")]')
    move_to_in_progress_button.click()

    web_page_data =  driver.page_source
    assert "Mark as Completed" in web_page_data 
    assert "Move to In Progress" not in web_page_data    
    
    # Move test item as complete
    mark_as_complete_button = driver.find_element_by_xpath('//a[@class="btn btn-success"][contains(., "Mark as Completed")]')
    mark_as_complete_button.click()
    web_page_data =  driver.page_source
    assert "Mark as Completed" not in web_page_data 
    assert "Back to Not Started" in web_page_data    
   
    # Move test item Back to Not Started
    back_to_not_started_button = driver.find_element_by_xpath('//a[@class="btn btn-light"][contains(., "Back to Not Started")]')
    back_to_not_started_button.click()
    web_page_data =  driver.page_source
    assert "Back to Not Started" not in web_page_data    
    assert "Move to In Progress" in web_page_data 
