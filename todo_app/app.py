
from flask import Flask, render_template, redirect, request
from todo_app.flask_config import Config, TrelloConfig
from todo_app.data.forms import TodoForm
from todo_app.data.trello import TrelloUtility
from todo_app.data.item import Item
from todo_app.data.session_items import get_item, save_item, remove_item


app = Flask(__name__)
app.config.from_object(Config)
trello_util = TrelloUtility(TrelloConfig.TRELLO_API_KEY, TrelloConfig.TRELLO_TOKEN)

def taskSort(item):
    return item.status

@app.route('/', methods=['GET'])
def index():
    form = TodoForm()
    items = []
    cards = trello_util.get_cards().json()['cards']
    for item in cards:
        id = item['id']
        title = item['name']
        list_id = item['idList']
        status = trello_util.get_status(list_id)
        items.append(Item(id, title, status))

    items.sort(reverse=True, key=taskSort)  
    
    return render_template('index.html', tasks=items, form=form)

@app.route('/', methods=['POST'])
def index_form():
    form = TodoForm()
    if form.validate_on_submit():
        title = request.form['title']
        list_id=trello_util.get_list_id(trello_util.STATUS_NOT_STARTED)
        trello_util.add_card(title, list_id)

    return redirect('/')            

@app.route('/complete/<id>', methods=['GET'])
def completed(id):
    trello_util.update_card(id, trello_util.STATUS_COMPLETED)

    return redirect ('/')

@app.route('/remove/<id>', methods=['GET'])
def remove_task(id):
    trello_util.delete_card(id)

    return redirect ('/')

if __name__ == '__main__':
    app.run()
