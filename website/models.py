#imports the init file db var
from enum import unique
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(500))
    credentials = db.relationship('Passwords')

#starting the passwords database
class Passwords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    username = db.Column(db.String(100))
    password = db.Column(db.String(200))
    #links the entries to a specific ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


