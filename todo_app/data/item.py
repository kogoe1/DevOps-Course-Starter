class Item:
    
    def __init__(self, id, title, status):
        self._id = id
        self._title = title
        self._status = status



    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def list_id(self):
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        self._list_id = list_id    


