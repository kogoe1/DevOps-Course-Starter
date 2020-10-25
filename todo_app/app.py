
from flask import Flask, render_template, redirect, request
from todo_app.flask_config import Config
from todo_app.data.forms import *
from todo_app.data.session_items import *


app = Flask(__name__)
app.config.from_object(Config)

def taskSort(item):
    return item['status']

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TodoForm()
    tasks = get_items()
    if form.validate_on_submit():
        title = request.form['title']
        add_item(title)
    tasks.sort(reverse=True, key=taskSort)
    return render_template('index.html', tasks=tasks, form=form)

@app.route('/complete/<id>', methods=['GET'])
def completed(id):
    item = get_item(id)
    item['status'] = 'Completed'
    save_item(item)

    return redirect ('/')

@app.route('/remove/<id>', methods=['GET'])
def remove_task(id):
    item = get_item(id)
    remove_item(item)

    return redirect ('/')


if __name__ == '__main__':
    app.run()
