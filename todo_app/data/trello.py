import requests
from requests.models import Response

class TrelloUtility:
    """ Consider making BOARD_ID dynamic"""
    BOARD_ID = "5fb51906cc7d395b1b145b0e" 
    member_url = "https://api.trello.com/1/members/me/boards?fields=name,url"
    BOARDS_URL = "https://api.trello.com/1/boards/" + BOARD_ID
    CARDS_URL = "https://api.trello.com/1/cards/"
    list_id_and_name_map = {}

    def __init__(self, api_key, token):
        self.key = api_key
        self.token = token

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

    def get_lists(self) -> Response:
         query = {
            'key': self.key,
            'token': self.token,
            'fields': 'name',
            'lists': 'all'
         }
         return self.api_call("GET", self.BOARDS_URL, query)

    def get_cards(self) -> Response:
        query = {
            'key': self.key,
            'token': self.token,
            'fields': 'name',
            'cards': 'all'
        }
        return self.api_call('GET', self.BOARDS_URL, query)

    def add_card(self, name, list_id) -> Response:
        query = {
            'key': self.key,
            'token': self.token,
            'name': name,
            'idList': list_id
        }
        return self.api_call('POST', self.CARDS_URL, query)

    def delete_card(self, card_id) -> Response:
        url = self.CARDS_URL + card_id
        query = {
            'key': self.key,
            'token': self.token,
        }
        return self.api_call('DELETE', url, query)

    def get_status(self, list_id) -> str:
        list_name = self.list_id_and_name_map[list_id]
        if list_name == 'To Do':
            return "Not Started" 
        elif list_name == 'Doing':
            return "In Progress"
        elif list_name == 'Done':
            return "Completed"
        else: 
            return  "No Status"                     

    def get_list_id(self, status) -> str:
        list_id_and_name_pair_list = self.list_id_and_name_map.items()
        for list_id, name in list_id_and_name_pair_list:
            if name == self.get_list_name_from_status(status):
                return list_id

    def get_list_name_from_status(self, status) -> str:
        if status == 'Not Started':
            return "To Do"
        if status == 'In Progress':
            return "Doing"
        if status == 'Completed':
            return "Done"
