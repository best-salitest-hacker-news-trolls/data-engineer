
from flask import Flask, request
from .models import DB, UserModel, Comment
import psycopg2
import os

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'buildweek3.sqlite3'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello to make sure it works
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/user/<name>')
    def user_salt_score(name=None):
        name = name or request.values['user_name']
        return "To be Implemented "  # return the salt score corresponding to
    @app.route('/leader_board')
    def leader_board():
        # return the top saltiest users in our database
        pass

    # elephantSQL Info
# Server: rajje.db.elephantsql.com (rajje-01)
# user: bdnyvcca 
# password: v_OUkGHLr2HjMoxT_LWFhd5tYZh4jsxm
# URL: postgres://bdnyvcca:v_OUkGHLr2HjMoxT_LWFhd5tYZh4jsxm@rajje.db.elephantsql.com:5432/bdnyvcca
# API Key: 44c09cc1-ae32-4d58-bbac-26d33bbb2890
# >>>>>>> cf5eda54ce7a2575d408c1fbc60ce0a034a6a350
