from flask import Blueprint

discounts_bp = Blueprint('discounts', __name__)

from . import routes