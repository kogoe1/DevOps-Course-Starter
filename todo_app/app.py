
from flask import Flask, url_for, render_template, redirect, flash, request
from todo_app.flask_config import Config
from todo_app.data.forms import *
from todo_app.data.session_items import *


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TodoForm()
    tasks = get_items()
    if form.validate_on_submit():
        title = request.form['title']
        add_item(title)

    return render_template('index.html', tasks=tasks, form=form)

@app.route('/complete/<id>', methods=['GET'])
def completed(id):
    item = get_item(id)
    item['status'] = 'Completed'
    save_item(item)

    return redirect ('/')


if __name__ == '__main__':
    app.run()
