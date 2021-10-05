from typing import List
import requests
from requests.models import Response
from todo_app.data.item import Item
from todo_app.data.storage_interface import StorageUtilityInterface

class TrelloUtility(StorageUtilityInterface):
    BOARD_URL = "https://api.trello.com/1/boards/"
    CARDS_URL = "https://api.trello.com/1/cards/"
    STATUS_NOT_STARTED = "Not Started"
    STATUS_IN_PROGRESS = "In Progress"
    STATUS_COMPLETED = "Completed"
    list_id_and_name_map = {}

    def __init__(self, api_key, token, board_id):
        self.key = api_key
        self.token = token 
        self.BOARD_URL = self.BOARD_URL + board_id


    def check_and_initialise_list_id_and_name_map(self):
        if len(self.list_id_and_name_map) == 0:
            lists = self.get_lists().json()['lists']
            for list in lists:
                list_id = list['id']
                list_name = list['name']
                self.list_id_and_name_map[list_id] = list_name

    def api_call(self, method, url, query) -> Response:
        response = requests.request(
            method,
            url,
            params=query
        )
        return response

    def api_call_with_header(self, method, url, headers, query) -> Response:
        response = requests.request(
            method,
            url,
            headers=headers,
            params=query
        )
        return response

    def get_lists(self) -> Response:
         query = {
            'key': self.key,
            'token': self.token,
            'fields': 'name',
            'lists': 'all'
         }
         return self.api_call("GET", self.BOARD_URL, query)
    
    def get_items(self) -> List[Item]:
        query = {
            'key': self.key,
            'token': self.token,
            'fields': 'name',
            'cards': 'all'
        }
        json_response = self.api_call('GET', self.BOARD_URL, query).json()
        
        items = []
        cards = json_response['cards']
        for item in cards:
            id = item['id']
            title = item['name']
            list_id = item['idList']
            description = item['desc']
            last_activity_date = item['dateLastActivity']
            status = self.get_status(list_id)
            items.append(Item(id, title, description, status, last_activity_date))

        return items    

    def add_item(self, name, description) -> Response:
        list_id = self.get_list_id(self.STATUS_NOT_STARTED)
        query = {
            'key': self.key,
            'token': self.token,
            'name': name,
            'idList': list_id,
            'desc': description
        }
        return self.api_call('POST', self.CARDS_URL, query)

    def delete_item(self, card_id) -> Response:
        url = self.CARDS_URL + card_id
        query = {
            'key': self.key,
            'token': self.token,
        }
        return self.api_call('DELETE', url, query)

    def update_item(self, card_id, status) -> Response:
        url = self.CARDS_URL + card_id
        list_id = self.get_list_id(status)
        query = {
            'key': self.key,
            'token': self.token,
            'idList': list_id
        }
        headers = {
            'Accept': 'application/json'
        }
        return self.api_call_with_header('PUT', url, headers, query)    

    def get_status(self, list_id) -> str:
        self.check_and_initialise_list_id_and_name_map() 

        list_name = self.list_id_and_name_map[list_id]
        if list_name == 'To Do':
            return self.STATUS_NOT_STARTED 
        elif list_name == 'Doing':
            return self.STATUS_IN_PROGRESS
        elif list_name == 'Done':
            return self.STATUS_COMPLETED
        else: 
            return  "No Status"                     

    def get_list_id(self, status) -> str:
        self.check_and_initialise_list_id_and_name_map() 

        list_id_and_name_pair_list = self.list_id_and_name_map.items()
        for list_id, name in list_id_and_name_pair_list:
            if name == self.get_list_name_from_status(status):
                return list_id

    def get_list_name_from_status(self, status) -> str:
        if status == self.STATUS_NOT_STARTED:
            return "To Do"
        if status == self.STATUS_IN_PROGRESS:
            return "Doing"
        if status == self.STATUS_COMPLETED:
            return "Done"
