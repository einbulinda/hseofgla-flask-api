from flask import Flask, redirect, url_for
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
    from .api import auth_bp, staff_bp, customer_bp, category_bp, product_bp, discounts_bp, orders_bp

    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(staff_bp, url_prefix='/api/v1/staff')
    app.register_blueprint(customer_bp, url_prefix='/api/v1/customer')
    app.register_blueprint(category_bp, url_prefix='/api/v1/category')
    app.register_blueprint(product_bp, url_prefix='/api/v1/product')
    app.register_blueprint(discounts_bp, url_prefix='/api/v1/discounts')
    app.register_blueprint(orders_bp, url_prefix='/api/v1/order')

    #  Redirect homepage to products resource
    @app.route('/')
    def homepage():
        return redirect(url_for('product.get_products'))

    # Error Handlers
    from .errors import handle_404_error, handle_400_error, handle_500_error

    app.register_error_handler(400, handle_400_error)
    app.register_error_handler(404, handle_404_error)
    app.register_error_handler(500, handle_500_error)

    return app
