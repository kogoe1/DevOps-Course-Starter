#!/bin/sh
gunicorn -w 3 -b 0.0.0.0:$PORT "todo_app.app:create_app()"