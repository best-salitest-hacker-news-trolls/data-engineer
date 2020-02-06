<<<<<<< HEAD:app/models.py
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class UserModel(DB.Model):
    __tablename__ = 'users'
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(20), unique=True)
    Users_Salty_Score = DB.Column(DB.BigInteger, nullable=False)

    def __repr__(self):
        return '<UserModel {}>'.format(self.username)


class CommentModel(DB.Model):
    __tablename__ = 'comments'
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(500), nullable=False)
    username = DB.Column(DB.BigInteger, DB.ForeignKey('users.username'))

    def __repr__(self):
        return '<CommentModel {}>'.format(self.username)
=======
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

DB = SQLAlchemy()


class UserModel(DB.Model):
    __tablename__ = 'users'
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(20), unique=True)
    Users_Salty_Score = DB.Column(DB.BigInteger, nullable=False)

    def __repr__(self):
        return '<UserModel {}>'.format(self.username)


class CommentModel(DB.Model):
    __tablename__ = 'comments'
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(500), nullable=False)
    username = DB.Column(DB.BigInteger, ForeignKey('users.username'))

    def __repr__(self):
        return '<CommentModel {}>'.format(self.username)
>>>>>>> master:models.py
