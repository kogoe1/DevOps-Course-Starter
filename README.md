# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

[TRELLO_API_KEY], [TRELLO_TOKEN] and [BOARD_ID] variables should be added to the `.env` file for accessing the Trello API


## Selenium Tests
Selenium tests were done using Firefox browser. You may need to download geckodriver (from https://github.com/mozilla/geckodriver/releases) and make it available in your environment PATH.

You may need to run the below command to install selenium if not already installed (this will install all the depenedenies in pyproject.toml file that are not already installed)
```bash
$ poetry install
``` 

Run the below command from `todo_app` directory to run Selenium tets
```bash
$ poetry run pytest tests_e2e
```

## VCR Tests
To run vcr tests you may need to run poetry install. Running the below, if not done already, will install all the depenedenies in pyproject.toml file that are not already installed
```bash
$ poetry install
```
Create a test board in Trello and add items at various stages (i.e. Todo, Doing, Done). These will be used for the first time vcr tests are run. Add the below IDs to `.env` file(see README.md file) for the initial VCR tests.

[TODO_ITEM_ID] - this is a new/TODO item ID that will be moved to in-progress/Doing

[COMPLETED_ITEM_ID] - this is a completed/Done item ID that will be moved back to Not started

[IN_PROGRESS_ITEM_ID] - this is an in-progress/Doing item ID that will be moved to Completed/Done

[REMOVE_ITEM_ID] - this is a test item ID that will be removed

Run the below command from `todo_app` directory to run VCR tets
```bash
$ poetry run pytest tests/test_integration_vcr.py 
```

## Running the tests
The tests can be run by doing the below from `todo_app` directory

```bash
$ poetry run pytest tests
```

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.


## Running the App in a Virtual Machine
This app can be run in a virtual machnine by doing the below (assuming you have vagrant installed)

```bash
vagrant up
```

You can then check that the app is up - after the above command is ran to start the virtual machine - by visiting this link http://127.0.0.1:5000/ 


## Running the App in a Container Using Docker
Docker file has been created with configuration for PROD and DEV environments.
The app can be accessed from a browser at http://127.0.0.1:5000/ for any of the containers that are ran 

Run the below commands from the root directory to build and launch the app in production mode
```bash
docker build --target production --tag todo-app:prod .

docker run -d -p 5000:5000 --env-file .env todo-app:prod
```

To launch the app in development mode run the below commands to build and launch respectively
```bash
docker build --target development --tag todo-app:dev .

docker run -d --env-file .env -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/devops_mod5/todo_app todo-app:dev
```

You can also use the below docker-compose command to to launch the app in a container in development mode 
```bash
docker-compose up
```