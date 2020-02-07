from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

DB = SQLAlchemy()


class UserModel(DB.Model):
    __tablename__ = 'users'
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(20), unique=True)
    Users_Salty_Score = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '<UserModel {}>'.format(self.username)


class CommentModel(DB.Model):
    __tablename__ = 'comments'
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.BigInteger, ForeignKey('users.username'))
    text = DB.Column(DB.Unicode(500), nullable=False)
    Comment_Salty_Score = DB.Column(DB.Float, nullable=False)
    def __repr__(self):
        return '<CommentModel {}>'.format(self.username)
