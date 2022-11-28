"""
This files initaties the backend as a module
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    """
    This function actually creates the app
    """
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'some key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app=app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/views')
    app.register_blueprint(auth, url_prefix='/')

    
    return app
