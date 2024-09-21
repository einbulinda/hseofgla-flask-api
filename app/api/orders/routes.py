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

    new_order, error = OrderService.create_order(order_data)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "Order placed successfully.",
        "data": new_order.to_dict()
    }), 201
