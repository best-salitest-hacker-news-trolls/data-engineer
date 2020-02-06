from flask import Flask, request, jsonify
from .models import DB, UserModel, CommentModel
from sqlalchemy import desc
import psycopg2
import os


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # this needs to be changed to PostGres or whatever we are using
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

    # send individual user, returns all of their comments
    # return
    @app.route('/user/<name>', methods=['GET'])
    def one_user_comments(name):
        name = name or request.values['user_name']
        # to query records which belong to a data model, write
        # [MODEL].query.[method].[FIRST or ALL]
        # https://hackersandslackers.com/flask-sqlalchemy-database-models
        # https://hackersandslackers.com/database-queries-sqlalchemy-orm/
        # this should return a
        person = CommentModel.query.filter(CommentModel.username == name).all()
        person_dict = person.__dict__
        return jsonify(person_dict)

    @app.route('/leader_board')
    def user_leader_board():
        # cut-off number to limit return
        # https://stackoverflow.com/questions/20642497/sqlalchemy-query-to
        # -return-only-n-results
        cutoff = 50
        # column with which to rank
        # https://stackoverflow.com/questions/4186062/sqlalchemy-order-by
        # -descending
        criteria = UserModel.Users_Salty_Score
        # return the top saltiest users in our database
        # not sure how to fix this being too long for PEP8
        people = UserModel.query.filter().limit(cutoff).all().order_by(
            desc(criteria))
        people_dict = people.__dict__
        return jsonify(people_dict)

    @app.route('/user/<name>/comments')
    def user_comment_ranks(name):

        return "Error"
    return app

# elephantSQL Info
# Server: rajje.db.elephantsql.com (rajje-01)
# user: bdnyvcca 
# password: v_OUkGHLr2HjMoxT_LWFhd5tYZh4jsxm
# URL: postgres://bdnyvcca:v_OUkGHLr2HjMoxT_LWFhd5tYZh4jsxm@rajje.db
# .elephantsql.com:5432/bdnyvcca
# API Key: 44c09cc1-ae32-4d58-bbac-26d33bbb2890
# >>>>>>> cf5eda54ce7a2575d408c1fbc60ce0a034a6a350
