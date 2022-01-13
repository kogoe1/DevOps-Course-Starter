from todo_app.data.trello import TrelloUtility
from todo_app.data.mongodb import MongoDbUtility
import os

class Storage:

    @staticmethod
    def getStorageUtility():
        storage_type = os.environ.get('STORAGE_TYPE')

        if storage_type == 'TRELLO':
            TRELLO_API_KEY=os.environ.get('TRELLO_API_KEY')
            TRELLO_TOKEN=os.environ.get('TRELLO_TOKEN')    
            BOARD_ID=os.environ.get('BOARD_ID')  
        
            trello_util = TrelloUtility(TRELLO_API_KEY, TRELLO_TOKEN, BOARD_ID)
            return trello_util
        elif storage_type == 'MONGO':
            return Storage.getMongoUtility()
        elif storage_type == 'AZURE_MONGO':
            return Storage.getAzureMongoUtility()
        else:
            # Default to MongoDB
            return Storage.getMongoUtility()


    @staticmethod
    def getMongoUtility():
        username = os.environ.get('MONGO_USERNAME')
        password = os.environ.get('MONGO_PASSWORD')
        mongo_url = os.environ.get('MONGO_URL')
        default_db = os.environ.get('DEFAULT_DB')

        mongoUtility =  MongoDbUtility(username, password, mongo_url, default_db)
        return mongoUtility    
    

    @staticmethod
    def getAzureMongoUtility():
        URL = os.environ.get('AZURE_MONGO_URL')
        DEFAULT_DB = os.environ.get('AZURE_MONGO_DB')
        URL_OPTIONS = os.environ.get('AZURE_MONGO_URL_OPTIONS')
        URI = URL + DEFAULT_DB + URL_OPTIONS
        mongoUtility =  MongoDbUtility(URI)

        return mongoUtility    

