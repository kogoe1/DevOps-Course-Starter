
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
        completed_items = []
        for item in self._items:
            if item.status == "Completed":
                completed_items.append(item)

        return completed_items
