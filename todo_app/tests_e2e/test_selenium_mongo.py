import os
from threading import Thread

import pytest
import requests
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from todo_app import app, data

from todo_app.data.storage import Storage

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')


@pytest.fixture(scope='module')
def test_app():

    file_path = find_dotenv('.env')
    # load_dotenv(file_path, override=True)
    load_dotenv(file_path)

    # Use a test db
    os.environ['DEFAULT_DB'] = 'test_todo_db'

    # construct the new application
    application = app.create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False)) 
    thread.daemon = True
    thread.start()
    yield app

    # Tear Down
    thread.join(1) 
    delete_test_db_data()
  
      
def delete_test_db_data():
    # Assuming db is Mongo 
    storage_utility = Storage.getStorageUtility()
    items = storage_utility.get_items()

    for item in items:
        id = item.id
        storage_utility.delete_item(id)

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
    assert "Mark as Completed" not in web_page_data    

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
