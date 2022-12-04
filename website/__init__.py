"""
The main file of the projects/backend.

This files initaties the backend as a module.
"""
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    """
    This function actually creates the app
    """
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'some key'  # type: ignore
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # type: ignore
    db.init_app(app=app)

    from .models import User, Notes
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/views')
    app.register_blueprint(auth, url_prefix='/')

    crete_database(app=app)
    return app

def crete_database(app):
    if not os.path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('DataBase created.')
