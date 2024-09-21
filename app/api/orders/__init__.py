from flask import Blueprint

orders_bp = Blueprint('order', __name__)

from . import routes