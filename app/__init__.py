from flask import Flask
from os import path

from .config import DefaultConfig
from .extensions import db, login_manager

from .auth import auth
from .views import views
from .models import User

BLUEPRINTS = [views, auth]

def create_app():
    app = Flask(__name__)

    configure_app(app)
    configure_blueprints(app, BLUEPRINTS)
    configure_extension(app)
    configure_database(app)

    return app

def configure_app(app):
    app.config.from_object(DefaultConfig)
    
def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def configure_extension(app):
    db.init_app(app)

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

def configure_database(app):
    if not path.exists('instance/' + DefaultConfig.DB_NAME):
        with app.app_context():
            db.create_all()
            print('Database Created')
        