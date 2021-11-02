from todo_app.data.storage_interface import StorageUtilityInterface
import pymongo
import datetime
from bson.objectid import ObjectId
from todo_app.data.item import Item
from todo_app.data.item_status import ItemStatus


class MongoDbUtility(StorageUtilityInterface):

    def __init__(self, username, password, mongo_url, default_db) -> None:
        super().__init__()
        self.client = pymongo.MongoClient("mongodb+srv://" + username + ":" + password + "@" + mongo_url + "/" + default_db + "?retryWrites=true&w=majority")
        self.db = self.client.get_default_database()
        pass


    def get_items(self):
        items = []

        collections = self.db.list_collection_names()
        for collection in collections:
            todo_collection_list = self.db_collection(collection).find({})
            for item in todo_collection_list:
                if item is not None:
                    id = item["_id"]
                    title = item["title"]
                    description = item["description"]
                    status = self.get_status_from_collection(collection)
                    retrieved_last_activity_date = item["lastActivityDate"]
                    last_activity_date = self.formated_last_activity_date(retrieved_last_activity_date)
                    items.append(Item(id, title, description, status, last_activity_date))

        return items


    def add_item(self, title:str, description:str):
        status = ItemStatus.NOT_STARTED
        new_item  = {
            "title": title,
            "description": description,
            "lastActivityDate": datetime.datetime.now()
        }

        collection = self.status_collection(status)
        return  collection.insert_one(new_item).inserted_id


    def update_item(self, id:str, status):
        destination_collection = self.status_collection(status)  
        retrieved_item = self.get_item_by_id(id)
        source_status = retrieved_item.status
        source_collection = self.status_collection(source_status)

        db_id = ObjectId(id)

        item_to_move = {
            "_id": db_id,
            "title": retrieved_item.title,
            "description": retrieved_item.description,
            "lastActivityDate": datetime.datetime.now()
        }

        query = {"_id": db_id}
        source_collection.delete_one(query)

        return destination_collection.insert_one(item_to_move).inserted_id        


    def delete_item(self, id:str):
        retrieved_item = self.get_item_by_id(id)
        source_status = retrieved_item.status
        source_collection = self.status_collection(source_status)
        query = {"_id": ObjectId(id)}
        return source_collection.delete_one(query)


    def status_collection(self, status):
        if (status == ItemStatus.NOT_STARTED):
            return self.db.not_started
            
        if (status == ItemStatus.IN_PROGRESS):
            return self.db.in_progress
        
        if (status == ItemStatus.COMPLETED):
            return self.db.completed


    def get_status_from_collection(self, collection):
        if collection == "not_started":
            return ItemStatus.NOT_STARTED

        if collection == "in_progress":
            return ItemStatus.IN_PROGRESS

        if collection == "completed":
            return ItemStatus.COMPLETED


    def db_collection(self, collection):
        if (collection == "not_started"):
            return self.db.not_started
            
        if (collection =="in_progress"):
            return self.db.in_progress
        
        if (collection == "completed"):
            return self.db.completed                      


    def get_item_by_id(self, search_id:str):
        items = self.get_items()
        for item in items:
            id = item.id
            if id == ObjectId(search_id):
                return item


    def formated_last_activity_date(self, lastActivityDate):
        if isinstance(lastActivityDate, datetime.datetime):
            return lastActivityDate.strftime("%Y-%m-%dT%H:%M:%SZ")    
        else:
            return lastActivityDate
