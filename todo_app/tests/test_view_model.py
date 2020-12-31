from todo_app.data.model import ViewModel
from todo_app.data.item import Item


class TestViewModel:

    @staticmethod
    def test_get_only_todo_items():
        #Arrange
        items = []
        item1 = Item(1,"Create View Model", "New model class", "Not Started")
        item2 = Item(2,"Create second item", "Second item", "In Progress")

        items.append(item1)
        items.append(item2)
        view_model = ViewModel(items)

        #Act
        items_view_model = view_model.todo_items

        #Assert
        assert len(items_view_model) == 1


    @staticmethod
    def test_get_only_in_progress_items():
        #Arrange
        items = []
        item1 = Item(1,"Create View Model", "New model class", "Not Started")
        item2 = Item(2,"Create second item", "Second item", "In Progress")

        items.append(item1)
        items.append(item2)
        view_model = ViewModel(items)

        #Act
        items_view_model = view_model.in_progress_items

        #Assert
        assert len(items_view_model) == 1 


    @staticmethod
    def test_get_only_completed_items():
        #Arrange
        items = []
        item1 = Item(1,"Create View Model", "New model class", "Not Started")
        item2 = Item(2,"Create second item", "Second item", "In Progress")
        item3 = Item(3,"Create Completed item", "Completed item", "Completed")

        items.append(item1)
        items.append(item2)
        items.append(item3)
        view_model = ViewModel(items)

        #Act
        items_view_model = view_model.completed_items

        #Assert
        assert len(items_view_model) == 1     