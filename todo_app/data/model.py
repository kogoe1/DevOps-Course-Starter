import datetime

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self): 
        return self._items


    @property
    def todo_items(self):
        todo_items = []
        for item in self._items:
            if item.status == "Not Started":
                todo_items.append(item)

        return todo_items


    @property
    def in_progress_items(self):
        in_porgress_items = []
        for item in self._items:
            if item.status == "In Progress":
                in_porgress_items.append(item)

        return in_porgress_items
    

    @property
    def completed_items(self):
        return self.get_completed_items()

    @property
    def total_completed_items(self):
        number_completed_items = len(self.get_completed_items())
        return number_completed_items   
    
    
    @property
    def show_all_done_items(self):
        items_to_show = []
        completed_items = self.get_completed_items()

        if len(completed_items) < 5:
            items_to_show = completed_items
        else:
            items_to_show = self.recent_done_items  

        return items_to_show

    def get_completed_items(self):
        completed_items = []
        for item in self._items:
            if item.status == "Completed":
                completed_items.append(item)
        return completed_items

    @property
    def recent_done_items(self):
        recently_completed_items = []
        completed_items = self.get_completed_items()
        for item in completed_items:
            if self.lastAcitivityDateIsToday(item):
                recently_completed_items.append(item)

        return recently_completed_items
    
    @property
    def older_done_items(self):
        older_completed_items = []
        completed_items = self.get_completed_items()
        for item in completed_items:
            if not self.lastAcitivityDateIsToday(item):
                older_completed_items.append(item)

        return older_completed_items


    def lastAcitivityDateIsToday(self, item) -> bool:
        today = datetime.date.today().isoformat()
        item_last_activity_date = item.last_activity_date[0:10]

        return today == item_last_activity_date   
