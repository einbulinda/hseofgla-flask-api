from flask import Blueprint

# Define Blueprint
staff_bp = Blueprint('staff', __name__)

# Import the routes to register them with the blueprints
from . import routes
