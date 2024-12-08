from . import orders_bp
from app.utils import roles_required
from flask_jwt_extended import get_jwt_identity, get_jwt
from flask import request, jsonify
from app.services import OrderService


@orders_bp.route('/', methods=['POST'])
@roles_required('customer', 'admin', 'staff')
def place_order():
    user = get_jwt_identity()
    order_data = request.get_json()
    order_data['created_by'] = user

    claims = get_jwt()
    is_customer = claims.get('role', None)
    if is_customer == 'customer':
        order_data['customer_id'] = user

    new_order, error, status_code = OrderService.create_order(order_data)

    if error:
        return jsonify({"error": error}), status_code

    return jsonify({
        "message": "Order placed successfully.",
        "data": new_order.to_dict()
    }), status_code


@orders_bp.route('/<int:order_id>', methods=['GET'])
@roles_required('admin', 'staff')
def get_an_order(order_id):
    order, error, status_code = OrderService.get_order_by_id(order_id)

    if error:
        return jsonify({"error": error}), status_code

    return jsonify({"data": order.to_dict()}), status_code


@orders_bp.route('/', methods=['GET'])
@roles_required('admin', 'staff')
def get_orders_list():
    orders, error, status_code = OrderService.get_orders()

    if error:
        return jsonify({"error": error}), status_code

    return jsonify({"data": [order.to_dict() for order in orders]}), status_code


