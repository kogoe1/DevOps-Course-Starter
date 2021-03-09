class Item:
    
    def __init__(self, id, title, description, status, last_activity_date):
        self._id = id
        self._title = title
        self._description = description
        self._status = status
        self._last_activity_date = last_activity_date


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
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def last_activity_date(self):
        return self._last_activity_date