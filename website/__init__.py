from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# create database 
db = SQLAlchemy()
DB_NAME = 'items.db'
bcrypt = Bcrypt()

def create_app():
    # Create the flask app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '55258efedbe4608330a7271c'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    bcrypt.init_app(app)
    app.app_context().push()

    # import and register blueprint
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import Items
        
    
    return app

