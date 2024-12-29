from flask import request, jsonify
from . import customer_bp
from app.utils import roles_required
from app.services import CustomerService
from app.errors import DetailedErrorResponse
from app.schemas.customer_schema import CustomerSchema


@customer_bp.route('/', methods=['POST'])
def register_customer():
    try:
        data = request.get_json()
        errors = CustomerSchema.validate_input(data)

        if errors:
            raise DetailedErrorResponse(400, "Validation Errors", errors)

        customer = CustomerService.register_customer(
            name=data.get('name'),
            mobile_number=data.get('mobile_number'),
            email=data.get('email'),
            created_by=data.get('created_by'),
            username=data.get('username'),
            password=data.get('password')
        )

        return jsonify({
            "message": "Customer created successfully",
            "data": customer.to_dict()
        }), 201
    except DetailedErrorResponse as error:
        return error.response, error.code
    except Exception as e:
        return DetailedErrorResponse(500, "Unexpected Error", str(e)).response, 500


@customer_bp.route('/<int:customer_id>', methods=['PUT'])
@roles_required('staff', 'admin')
def update_customer(customer_id):
    try:
        data = request.get_json()
        errors = CustomerSchema.validate_input(data)

        if errors:
            raise DetailedErrorResponse(400, "Validation Errors", errors)

        updated_customer = CustomerService.update_customer(
            customer_id,
            name=data.get('name'),
            mobile_number=data.get('mobile_number'),
            email=data.get('email'),
            updated_by=data.get('updated_by')
        )

        if not updated_customer:
            raise DetailedErrorResponse(404, "Customer not found.", f"Customer with ID {customer_id} not found")

        return jsonify({
            "message": "Customer updated successfully.",
            "data": updated_customer.to_dict()
        }), 200
    except DetailedErrorResponse as error:
        return error.response, error.code
    except Exception as e:
        return DetailedErrorResponse(500, "Unexpected Error", str(e)).response, 500


@customer_bp.route('/<int:customer_id>', methods=['GET'])
@roles_required('staff', 'admin')
def get_customer(customer_id):
    try:
        customer = CustomerService.get_customer_by_id(customer_id)
        if not customer:
            raise DetailedErrorResponse(404, "Customer not found.", f"Customer with ID {customer_id} not found")

        return jsonify({"data": customer.to_dict()}), 200
    except DetailedErrorResponse as error:
        return error.response, error.code
    except Exception as e:
        return DetailedErrorResponse(500, "Unexpected Error", str(e)).response, 500


@customer_bp.route('/', methods=['GET'])
@roles_required('staff', 'admin')
def get_customers():
    try:
        customers = CustomerService.get_all_customers()
        return jsonify({
            "data": [customer.to_dict() for customer in customers]
        }), 200
    except DetailedErrorResponse as error:
        return error.response, error.code
    except Exception as e:
        return DetailedErrorResponse(500, "Unexpected Error", str(e)).response, 500
