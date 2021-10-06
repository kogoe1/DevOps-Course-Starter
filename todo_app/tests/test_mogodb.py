from todo_app.data.mongodb import MongoDbUtility
import pytest
import os
from todo_app.data.item_status import ItemStatus

from dotenv import load_dotenv, find_dotenv

@pytest.fixture
def mongoUtility():

    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    username = os.environ.get('MONGO_USERNAME')
    password = os.environ.get('MONGO_PASSWORD')
    mongo_url = os.environ.get('MONGO_URL')
    default_db = os.environ.get('DEFAULT_DB')

    mongoUtility =  MongoDbUtility(username, password, mongo_url, default_db) 
    yield mongoUtility

    
def test_get_items(mongoUtility):  
    title = "Test todo item"
    description = "my test todo item"    
    item_id = mongoUtility.add_item(title, description)

    items = mongoUtility.get_items()  

    assert items is not None
    num_items = len(items)
    assert num_items > 0

    mongoUtility.delete_item(item_id)


def test_add_new_item(mongoUtility):  
    title = "Test todo item"
    description = "my test todo item"
        
    item_id = mongoUtility.add_item(title, description)

    added_item = mongoUtility.get_item_by_id(item_id)

    assert added_item.title == title
    assert added_item.status == ItemStatus.NOT_STARTED   

    mongoUtility.delete_item(item_id)
  

def test_update_item(mongoUtility):   
    title = "Test updated item 2"
    description = "test updated description 2"
    
    item_id = mongoUtility.add_item(title, description)

    mongoUtility.update_item(item_id, ItemStatus.IN_PROGRESS)

    updated_item = mongoUtility.get_item_by_id(item_id)

    assert updated_item.status == ItemStatus.IN_PROGRESS 
    assert updated_item.title == title
    mongoUtility.delete_item(item_id) 


def test_delete_item(mongoUtility):
    title = "Test delete item"
    description = "test delete item description 2"

    item_id = mongoUtility.add_item(title, description)

    added_item = mongoUtility.get_item_by_id(item_id)

    assert added_item.title == title
    mongoUtility.delete_item(item_id)
    id_after_delete = mongoUtility.get_item_by_id(item_id)
    assert id_after_delete is None 