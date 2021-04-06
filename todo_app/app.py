
from todo_app.data.model import ViewModel
from flask import Flask, render_template, redirect, request
# from todo_app.flask_config import Config, TrelloConfig
from todo_app.data.forms import TodoForm
from todo_app.data.trello import TrelloUtility
from todo_app.data.model import ViewModel

from dotenv import load_dotenv, find_dotenv

import os


app = Flask(__name__)

file_path = find_dotenv('.env')
load_dotenv(file_path, override=True)

app.config.from_object('todo_app.flask_config.Config')
    

TRELLO_API_KEY=os.environ.get('TRELLO_API_KEY')
TRELLO_TOKEN=os.environ.get('TRELLO_TOKEN')    
BOARD_ID=os.environ.get('BOARD_ID')  
    
trello_util = TrelloUtility(TRELLO_API_KEY, TRELLO_TOKEN, BOARD_ID)

def taskSort(item):
        return item.status

@app.route('/', methods=['GET'])
def index():
    form = TodoForm()
    items = trello_util.get_items()
    items.sort(reverse=True, key=taskSort)  
        
    item_view_model = ViewModel(items)
    return render_template('index.html', view_model=item_view_model, form=form)

@app.route('/', methods=['POST'])
def index_form():
    form = TodoForm()
    if form.validate_on_submit():
        title = request.form['title']
        description = request.form['description']
        trello_util.add_item(title, description)

    return redirect('/')            

@app.route('/in_progress/<id>', methods=['GET'])
def in_progress(id):
    trello_util.update_item(id, trello_util.STATUS_IN_PROGRESS)

    return redirect ('/')

@app.route('/complete/<id>', methods=['GET'])
def completed(id):
    trello_util.update_item(id, trello_util.STATUS_COMPLETED)

    return redirect ('/')

@app.route('/not_started/<id>', methods=['GET'])
def not_started(id):
    trello_util.update_item(id, trello_util.STATUS_NOT_STARTED)

    return redirect ('/')

@app.route('/remove/<id>', methods=['GET'])
def remove_task(id):
    trello_util.delete_item(id)

    return redirect ('/')


if __name__ == '__main__':
    app.run()
