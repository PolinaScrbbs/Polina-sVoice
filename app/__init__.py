from flask import Flask

from .config import Config
from .database import db

from .routers.main import main

def create_app(config_class: object = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(main)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

