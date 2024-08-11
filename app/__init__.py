from flask import Flask
from app.config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Initialize extensions (SQLAlchemy, JWT, etc.)
    # Register Blueprints
    # Other app setup code

    return app
