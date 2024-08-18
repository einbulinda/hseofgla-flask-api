from flask import request, jsonify
from . import customer_bp
from app.utils import roles_required
from app.services import CustomerService


@customer_bp.route('/', methods=['POST'])
def register_customer():
    data = request.get_json()
    customer, error = CustomerService.register_customer(
        name=data.get('name'),
        mobile_number=data.get('mobile_number'),
        email=data.get('email'),
        created_by=data.get('created_by'),
        username=data.get('username'),
        password=data.get('password')
    )

    if error:
        return jsonify({"error": error}), 400

    return jsonify(customer.to_dict()), 201


@customer_bp.route('/<int:customer_id>', methods=['PUT'])
@roles_required('staff', 'admin')
def update_customer(customer_id):
    data = request.get_json()
    updated_customer = CustomerService.update_customer(
        customer_id,
        name=data.get('name'),
        mobile_number=data.get('mobile_number'),
        email=data.get('email'),
        updated_by=data.get('updated_by')
    )

    if not updated_customer:
        return jsonify({"error": "Customer not found."}), 404

    return jsonify(updated_customer.to_dict()), 200


@customer_bp.route('/<int:customer_id>', methods=['GET'])
@roles_required('staff', 'admin')
def get_customer(customer_id):
    customer = CustomerService.get_customer_by_id(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify(customer.to_dict()), 200


@customer_bp.route('/', methods=['GET'])
@roles_required('staff', 'admin')
def get_customers():
    customers = CustomerService.get_all_customers()
    return jsonify([customer.to_dict() for customer in customers]), 200
