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
