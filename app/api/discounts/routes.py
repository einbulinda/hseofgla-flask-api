from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from . import discounts_bp
from app.utils import roles_required
from app.services import DiscountService


@discounts_bp.route('/', methods=['POST'])
@roles_required('admin')
def create_discount():
    discount_info = request.get_json()
    current_user = get_jwt_identity()
    discount_info['created_by'] = current_user
    new_discount, error = DiscountService.create_discount(discount_info)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "Discount created successfully.",
        "data": new_discount.to_dict()
    }), 201


@discounts_bp.route('/<int:discount_id>', methods=['PUT'])
@roles_required('admin')
def update_discount(discount_id):
    discount_info = request.get_json()
    current_user = get_jwt_identity()

    discount_info['updated_by'] = current_user

    discount, error = DiscountService.update_discount(discount_id, discount_info)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "Discount information updated successfully.",
        "data": discount.to_dict()
    })


@discounts_bp.route('/<int:discount_id>', methods=['GET'])
def fetch_discount(discount_id):
    discount, error = DiscountService.get_discount(discount_id)
    if error:
        return jsonify({"error": error}), 400

    return jsonify({"data": discount.to_dict()}), 200


@discounts_bp.route('/', methods=['GET'])
def fetch_discount_list():
    discounts, error = DiscountService.get_discounts()

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "data": [discount.to_dict() for discount in discounts]
    }), 200
