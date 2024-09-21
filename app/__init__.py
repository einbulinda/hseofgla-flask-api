from flask import Flask
from app.config import config_by_name
from app.extensions import db, migrate, jwt, ma
from app.models.staff import Staff
from app.logging_config import log_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Initialize extensions (SQLAlchemy, JWT, etc.)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)
    log_config()

    # Register Blueprints
    from .api.auth import auth_bp
    from .api.staff import staff_bp
    from .api.customers import customer_bp
    from .api.categories import category_bp
    from .api.products import product_bp
    from .api.discounts import discounts_bp

    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(staff_bp, url_prefix='/api/v1/staff')
    app.register_blueprint(customer_bp, url_prefix='/api/v1/customer')
    app.register_blueprint(category_bp, url_prefix='/api/v1/category')
    app.register_blueprint(product_bp, url_prefix='/api/v1/product')
    app.register_blueprint(discounts_bp, url_prefix='api/v1/discounts')

    # Error Handler Example

    # @app.errorhandler(404)
    # def nof_found(error):
    #     return jsonify({
    #         "error": "Not Found",
    #         "message": "The requested URL is not found on the server."
    #     }), 404
    return app
