
from functools import wraps
from todo_app.data.model import ViewModel
from flask import Flask, render_template, redirect, request
# from todo_app.flask_config import Config, TrelloConfig
from todo_app.data.forms import TodoForm
from todo_app.data.model import ViewModel
from todo_app.data.storage import Storage
from todo_app.data.item_status import ItemStatus


from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from oauthlib.oauth2 import WebApplicationClient
import os
import json
import requests
from todo_app.data.user import Roles, User
from flask.helpers import url_for


login_manager = LoginManager()
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
OAUTH_URL=os.environ.get('OAUTH_URL')
TOKEN_ENDPOINT=os.environ.get('TOKEN_ENDPOINT')
USER_INFO_ENDPOINT=os.environ.get('USER_INFO_ENDPOINT')


def create_app():
    app = Flask(__name__)

    app.config.from_object('todo_app.flask_config.Config')
        
    storage_utility = Storage.getStorageUtility()

    client = WebApplicationClient(CLIENT_ID)


    @app.route('/login', methods=['GET'])
    def login():
        request_uri =  client.prepare_request_uri(
            OAUTH_URL,
            redirect_uri=request.base_url + "/callback"
        )

        return redirect(request_uri)        
 
    @app.route("/login/callback")
    def callback():
        # Get authorization code Github sends back
        code = request.args.get('code')

        # Prepare and send a request to get tokens
        token_url, headers, body = client.prepare_token_request(
            TOKEN_ENDPOINT,
            # authorization_response=request.url,
            authorization_response=request.base_url,
            redirect_url=request.base_url,
            code=code
        )
        headers['Accept']='application/json'
        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(CLIENT_ID, CLIENT_SECRET)
        )

        # Parse the tokens!
        token_response_json = token_response.json()
        client.parse_request_body_response(json.dumps(token_response_json))

        uri, headers, body = client.add_token(USER_INFO_ENDPOINT)
        userinfo_response = requests.get(uri, headers=headers, data=body)

        if userinfo_response.ok:
            unique_id = userinfo_response.json()['id']
            user_login = userinfo_response.json()['login']
            user = User(unique_id)
        else:
            return "User not available or not verified", 400 

        # Begin user session by logging the user in
        login_user(user)

        # Send user back to homepage
        return redirect(url_for('index'))      


    @login_manager.unauthorized_handler
    def unauthenticated():
        # Redirect to the Github OAuth flow when unauthenticated
        return redirect (url_for('login'))
            

    @login_manager.user_loader
    def load_user(user_id):
        if user_id == '':
            return None
            
        return User(user_id)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("index"))
    
             
    login_manager.init_app(app) 


    def taskSort(item):
            return item.status

    def is_writer(current_user) -> bool:        
        if not current_user.is_anonymous:
            return current_user.get_role() == Roles.WRITER

        return False

    # Decorator to check that user has writer privilege
    def writer_role_required(func):

        @wraps(func)
        def decorated_view(*args, **kwargs):
            if is_writer(current_user):
                return func(*args, **kwargs)
            return "User NOT permited for this action", 400
        return decorated_view                      


    @app.route('/', methods=['GET'])
    @login_required
    def index():
        form = TodoForm()
        items = storage_utility.get_items()
        items.sort(reverse=True, key=taskSort)  
            
        item_view_model = ViewModel(items)

        # Default to Read Only Template 
        template_html = 'index_ro.html'

        if is_writer(current_user):
            template_html = 'index.html'
                
        return render_template(template_html, view_model=item_view_model, form=form)


    @app.route('/', methods=['POST'])
    @writer_role_required
    def index_form():
        form = TodoForm()
        if form.validate_on_submit():
            title = request.form['title']
            description = request.form['description']
            storage_utility.add_item(title, description)

        return redirect('/')            
   
    
    @app.route('/in_progress/<id>', methods=['GET'])
    @writer_role_required
    def in_progress(id):
        storage_utility.update_item(id, ItemStatus.IN_PROGRESS)
        return redirect ('/')
   

    @app.route('/complete/<id>', methods=['GET'])
    @writer_role_required
    def completed(id):
        storage_utility.update_item(id, ItemStatus.COMPLETED)

        return redirect ('/')

    @app.route('/not_started/<id>', methods=['GET'])
    @writer_role_required
    def not_started(id):
        storage_utility.update_item(id, ItemStatus.NOT_STARTED)

        return redirect ('/')

    @app.route('/remove/<id>', methods=['GET'])
    @writer_role_required
    def remove_task(id):
        storage_utility.delete_item(id)

        return redirect ('/')


    if __name__ == '__main__':
        app.run()

    return app