from todo_app.data.model import ViewModel
from todo_app.data.item import Item

import datetime


class TestViewModel:

    last_activity_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    
    @staticmethod
    def test_get_only_todo_items():
        #Arrange
        items = []
        item1 = Item(1,"Create View Model", "New model class", "Not Started", TestViewModel.last_activity_date)
        item2 = Item(2,"Create second item", "Second item", "In Progress", TestViewModel.last_activity_date)

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
        item1 = Item(1,"Create View Model", "New model class", "Not Started", TestViewModel.last_activity_date)
        item2 = Item(2,"Create second item", "Second item", "In Progress", TestViewModel.last_activity_date)

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
        item1 = Item(1,"Create View Model", "New model class", "Not Started", TestViewModel.last_activity_date)
        item2 = Item(2,"Create second item", "Second item", "In Progress", TestViewModel.last_activity_date)
        item3 = Item(3,"Create Completed item", "Completed item", "Completed", TestViewModel.last_activity_date)

        items.append(item1)
        items.append(item2)
        items.append(item3)
        view_model = ViewModel(items)

        #Act
        items_view_model = view_model.completed_items

        #Assert
        assert len(items_view_model) == 1     


    @staticmethod
    def test_show_all_done_items_when_they_are_less_than_five():
        #Arrange
        items = []
        item1 = Item(1,"Create View Model", "New model class", "Not Started", TestViewModel.last_activity_date)
        item2 = Item(2,"Create second item", "Second item", "In Progress", TestViewModel.last_activity_date)
        item3 = Item(3,"Create Completed item", "Completed item", "Completed", "2020-12-30T21:57:33.612Z")
        item4 = Item(4,"Create Another Completed item", "Another Completed item", "Completed", TestViewModel.last_activity_date)

        items.append(item1)
        items.append(item2)
        items.append(item3)
        items.append(item4)
        view_model = ViewModel(items)

        #Act
        items_view_model = view_model.show_all_done_items

        #Assert
        assert len(items_view_model) == 2         
    
    @staticmethod
    def test_show_only_recently_done_items_when_total_is_greater_than_five():
        #Arrange
        items = []
        item1 = Item(1,"Create View Model", "New model class", "Not Started", TestViewModel.last_activity_date)
        item2 = Item(2,"Create second item", "Second item", "In Progress", TestViewModel.last_activity_date)
        item3 = Item(3,"Create Completed item", "Completed item", "Completed", "2020-12-30T21:57:33.612Z")
        item4 = Item(4,"Create Another Completed item", "Another Completed item", "Completed", TestViewModel.last_activity_date)
        item5 = Item(5,"Create fith item", "Create item 5", "Completed", "2020-12-29T21:57:33.612Z")
        item6 = Item(6,"Create sixth item", "Create item 6", "Completed", "2020-12-28T21:57:33.612Z")
        item7 = Item(7,"Create seventh item", "Create item 7", "Completed", "2020-12-28T20:57:33.612Z")
        item8 = Item(8,"Create eighth item", "Create item 8", "Completed", "2020-12-26T20:30:33.612Z")

        items.append(item1)
        items.append(item2)
        items.append(item3)
        items.append(item4)
        items.append(item5)
        items.append(item6)
        items.append(item7)
        items.append(item8)
        view_model = ViewModel(items)

        #Act
        completed_items_view_model = view_model.show_all_done_items

        #Assert
        assert len(completed_items_view_model) == 1         
    
    @staticmethod
    def test_show_only_recently_done_items_when_total_is_greater_than_five_2():
        #Arrange
        items = []
        item1 = Item(1,"Create View Model", "New model class", "Not Started", TestViewModel.last_activity_date)
        item2 = Item(2,"Create second item", "Second item", "In Progress", TestViewModel.last_activity_date)
        item3 = Item(3,"Create Completed item", "Completed item", "Completed", "2020-12-30T21:57:33.612Z")
        item4 = Item(4,"Create Another Completed item", "Another Completed item", "Completed", TestViewModel.last_activity_date)
        item5 = Item(5,"Create fith item", "Create item 5", "Completed", "2020-12-29T21:57:33.612Z")
        item6 = Item(6,"Create sixth item", "Create item 6", "Completed", "2020-12-28T21:57:33.612Z")
        item7 = Item(7,"Create seventh item", "Create item 7", "Completed", "2020-12-28T20:57:33.612Z")
        item8 = Item(8,"Create eighth item", "Create item 8", "Completed", TestViewModel.last_activity_date)

        items.append(item1)
        items.append(item2)
        items.append(item3)
        items.append(item4)
        items.append(item5)
        items.append(item6)
        items.append(item7)
        items.append(item8)
        view_model = ViewModel(items)

        #Act
        recently_done_items_view_model = view_model.show_all_done_items

        #Assert
        assert len(recently_done_items_view_model) == 2         
    
    @staticmethod
    def test_show_only_older_done_items():
        #Arrange
        items = []
        item1 = Item(1,"Create View Model", "New model class", "Not Started", TestViewModel.last_activity_date)
        item2 = Item(2,"Create second item", "Second item", "In Progress", TestViewModel.last_activity_date)
        item3 = Item(3,"Create Completed item", "Completed item", "Completed", "2020-12-30T21:57:33.612Z")
        item4 = Item(4,"Create Another Completed item", "Another Completed item", "Completed", TestViewModel.last_activity_date)
        item5 = Item(5,"Create fith item", "Create item 5", "Completed", "2020-12-29T21:57:33.612Z")
        item6 = Item(6,"Create sixth item", "Create item 6", "Completed", "2020-12-28T21:57:33.612Z")
        item7 = Item(7,"Create seventh item", "Create item 7", "Completed", "2020-12-28T20:57:33.612Z")      
        item8 = Item(8,"Create eighth item", "Create item 8", "Completed", TestViewModel.last_activity_date)
       
        items.append(item1)
        items.append(item2)
        items.append(item3)
        items.append(item4)
        items.append(item5)
        items.append(item6)
        items.append(item7)
        items.append(item8)
        view_model = ViewModel(items)

        #Act
        older_items_view_model = view_model.older_done_items

        #Assert
        assert len(older_items_view_model) == 4         