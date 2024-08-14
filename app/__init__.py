from flask import Flask, jsonify
from app.config import config_by_name
from app.extensions import db, migrate, jwt, ma
from app.models.staff import Staff


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Initialize extensions (SQLAlchemy, JWT, etc.)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)

    # Register Blueprints
    from .api.auth import auth_bp
    from .api.staff import staff_bp

    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(staff_bp, url_prefix='/api/v1/staff')

    # Other app setup code

    # Set up basic route for testing
    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to House of Glamour API."
        })

    # Error Handler Example
    @app.errorhandler(404)
    def nof_found(error):
        return jsonify({
            "error": "Not Found",
            "message": "The requested URL is not found on the server."
        }), 404
    return app
