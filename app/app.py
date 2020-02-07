from flask import Flask, request, jsonify
from .models import DB, UserModel, CommentModel
from sqlalchemy import desc, create_engine
# import psycopg2
import os
import pandas as pd

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db2.sqlite3'
    DB.init_app(app)
    # look up later why this is needed to create table here
    # https://stackoverflow.com/questions/46540664/no-application-found-either-work-inside-a-view-function-or-push-an-application
    # with app.app_context():
    #     DB.create_all()
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)
    # get json turn into dataframe
    # ask Jordan how to make this url pep8 compliant
    url = 'https://raw.githubusercontent.com/best-salitest-hacker-news-trolls/machine-learning-engineers/master/10000_predictions_extra.json'
    df = pd.read_json(url)
    # create dataframe for comments table
    comment_df = df[['by','text','scores_sum']].copy()
    # create dataframe for users table
    # first by doing a group by 
    groupby_user = comment_df['scores_sum'].groupby(comment_df['by'])
    # then doing means since we use average saltiness not sum
    # and turn that series into a dataframe with reset_index
    user_df = groupby_user.mean().reset_index()
    # add comment_df to comments table
    comment_df.to_sql('comments', con=engine, if_exists='replace')
    print(
        'we habe',
        len(engine.execute("SELECT * FROM comments").fetchall())
    )
    user_df.to_sql('users', con=engine, if_exists='replace')
    


    # config stuff
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
        return str(comment_df)
    
    # accidently does the same thing as the other one
    # send individual user, returns all of their comments
    # return
    # @app.route('/user/<name>', methods=['GET'])
    # def one_user_comments(name):
    #     name = name or request.values['user_name']
    #     # to query records which belong to a data model, write
    #     # [MODEL].query.[method].[FIRST or ALL]
    #     # https://hackersandslackers.com/flask-sqlalchemy-database-models
    #     # https://hackersandslackers.com/database-queries-sqlalchemy-orm/
    #     # this should return a
    #     person = CommentModel.query.filter(CommentModel.username == name).all()
    #     person_dict = person.__dict__
    #     return jsonify(person_dict)

    # does not take any arguments and returns the leaderboard
    # change how many are returned with cutoff variable
    @app.route('/leader_board')
    def user_leader_board():
        # cut-off number to limit return
        # https://stackoverflow.com/questions/20642497/sqlalchemy-query-to
        # -return-only-n-results
        # cutoff = 50
        # column with which to rank
        # https://stackoverflow.com/questions/4186062/sqlalchemy-order-by
        # -descending
        # criteria = UserModel.Users_Salty_Score
        # return the top saltiest users in our database
        # not sure how to fix this being too long for PEP8
        people = engine.execute("SELECT by, scores_sum FROM users ORDER BY scores_sum DESC LIMIT 50").fetchall()
        #people = UserModel.query.filter().limit(cutoff).all().order_by(
            #desc(criteria))
        #people_dict = people.__dict__
        return jsonify(str(people))

    # returns all of a users' comments 
    @app.route('/user/<name>/comments')
    def user_comment_ranks(name):
        # number of items to return
        # cutoff = 10
        # query filter
        # criteria = UserModel.Users_Salty_Score
        # comments = UserModel.query(filter(UserModel.username == name)).limit(cutoff).all().order_by(desc(criteria))
        # comments_dict = comments.__dict__
        comments = engine.execute("SELECT by, text, scores_sum FROM comments WHERE by LIKE '" + name + "'").fetchall()
        # return jsonify(comments_dict)
        return jsonify(str(comments))

    return app

# elephantSQL Info
# Server: rajje.db.elephantsql.com (rajje-01)
# user: bdnyvcca 
# password: v_OUkGHLr2HjMoxT_LWFhd5tYZh4jsxm
# URL: postgres://bdnyvcca:v_OUkGHLr2HjMoxT_LWFhd5tYZh4jsxm@rajje.db
# .elephantsql.com:5432/bdnyvcca
# API Key: 44c09cc1-ae32-4d58-bbac-26d33bbb2890
# >>>>>>> cf5eda54ce7a2575d408c1fbc60ce0a034a6a350
