'''
This file handles the actual objects(users and their notes) of website.
'''
from . import db
from sqlalchemy import func
# from flask_login import UserMixin

class Notes(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class User(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(10000), nullable=False)
    password = db.Column(db.String(300), nullable=False)

    notes = db.relationship('Notes')
