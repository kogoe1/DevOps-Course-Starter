
from todo_app.data.model import ViewModel
from flask import Flask, render_template, redirect, request
# from todo_app.flask_config import Config, TrelloConfig
from todo_app.data.forms import TodoForm
from todo_app.data.model import ViewModel
from todo_app.data.storage import Storage
from todo_app.data.item_status import ItemStatus


def create_app():
    app = Flask(__name__)

    app.config.from_object('todo_app.flask_config.Config')
        
    storage_utility = Storage.getStorageUtility()

    def taskSort(item):
            return item.status

    @app.route('/', methods=['GET'])
    def index():
        form = TodoForm()
        items = storage_utility.get_items()
        items.sort(reverse=True, key=taskSort)  
            
        item_view_model = ViewModel(items)
        return render_template('index.html', view_model=item_view_model, form=form)

    @app.route('/', methods=['POST'])
    def index_form():
        form = TodoForm()
        if form.validate_on_submit():
            title = request.form['title']
            description = request.form['description']
            storage_utility.add_item(title, description)

        return redirect('/')            

    @app.route('/in_progress/<id>', methods=['GET'])
    def in_progress(id):
        storage_utility.update_item(id, ItemStatus.IN_PROGRESS)

        return redirect ('/')

    @app.route('/complete/<id>', methods=['GET'])
    def completed(id):
        storage_utility.update_item(id, ItemStatus.COMPLETED)

        return redirect ('/')

    @app.route('/not_started/<id>', methods=['GET'])
    def not_started(id):
        storage_utility.update_item(id, ItemStatus.NOT_STARTED)

        return redirect ('/')

    @app.route('/remove/<id>', methods=['GET'])
    def remove_task(id):
        storage_utility.delete_item(id)

        return redirect ('/')


    if __name__ == '__main__':
        app.run()

    return app