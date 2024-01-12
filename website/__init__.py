from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create database 
db = SQLAlchemy()
DB_NAME = 'items.db'

def create_app():
    # Create the flask app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # import and register blueprint
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import ItemsModel
    
    # create database for app
    with app.app_context():
        db.create_all()
    
    return app

