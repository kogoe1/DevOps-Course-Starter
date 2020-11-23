
from flask import Flask, render_template, redirect, request
from todo_app.flask_config import Config, TrelloConfig
from todo_app.data.forms import TodoForm
from todo_app.data.trello import TrelloUtility


app = Flask(__name__)
app.config.from_object(Config)
trello_util = TrelloUtility(TrelloConfig.TRELLO_API_KEY, TrelloConfig.TRELLO_TOKEN)

def taskSort(item):
    return item.status

@app.route('/', methods=['GET'])
def index():
    form = TodoForm()
    items = trello_util.get_items()
    items.sort(reverse=True, key=taskSort)  
    
    return render_template('index.html', tasks=items, form=form)

@app.route('/', methods=['POST'])
def index_form():
    form = TodoForm()
    if form.validate_on_submit():
        title = request.form['title']
        description = request.form['description']
        trello_util.add_item(title, description)

    return redirect('/')            

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
