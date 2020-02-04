<<<<<<< HEAD
from flask import Flask, request
from .models import DB, UserModel, Comment
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# takes in a user name and returns a salt score
@app.route('/user')
# models
@app.route('/user/<name>')
def user_salt_score(name=None):
    name = name or request.values['user_name']
    return "To be Implemented " # return the salt score corresponding to


# returns the leaderboard,
@app.route('/leaderboard')
def leaderboard():
    # return the top saltiest users in our database
    pass 
=======
from flask import Flask
import psycopg2
from flask import Request
import os

app = Flask(__name__)

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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app


@app.route('/user')
def user_salt_score():
    
    return 'Hello, World!'

# elephantSQL Info 
# Server: rajje.db.elephantsql.com (rajje-01)
# user: bdnyvcca 
# password: v_OUkGHLr2HjMoxT_LWFhd5tYZh4jsxm
# URL: postgres://bdnyvcca:v_OUkGHLr2HjMoxT_LWFhd5tYZh4jsxm@rajje.db.elephantsql.com:5432/bdnyvcca
# API Key: 44c09cc1-ae32-4d58-bbac-26d33bbb2890
>>>>>>> cf5eda54ce7a2575d408c1fbc60ce0a034a6a350
