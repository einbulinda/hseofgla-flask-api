from flask import request, jsonify
from . import staff_bp
from app.services.staff_service import StaffService


@staff_bp.route('/', methods=['POST'])
def create_staff():
    data = request.get_json()
    name = data.get('name')
    role = data.get('role')
    mobile_number = data.get('mobile_number')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    created_by = data.get('created_by')

    staff, error = StaffService.create_staff(name, role, mobile_number, email, username, password, created_by)
    if error:
        return jsonify({"error": error}), 400

    return jsonify({"message": "Staff member created successfully", "staff_id": staff.staff_id}), 201


@staff_bp.route('/staff/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    data = request.get_json()
    name = data.get('name')
    role = data.get('role')
    mobile_number = data.get('mobile_number')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    updated_by = data.get('updated_by')

    staff, error = StaffService.update_staff(staff_id, name, role, mobile_number, email, username, password, updated_by)
    if error:
        return jsonify({"error": error}), 400

    return jsonify({"message": "Staff member updated successfully", "staff_id": staff.staff_id}), 200

