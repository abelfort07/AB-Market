from flask import Flask


def create_app():
    # Create the flask app
    app = Flask(__name__)

    # import and register blueprint
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app

