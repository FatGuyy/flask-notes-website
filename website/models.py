from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):  # type: ignore #This comment is for pylance, no code
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))