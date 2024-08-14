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


@staff_bp.route('/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    data = request.get_json()
    name = data.get('name')
    role = data.get('role')
    mobile_number = data.get('mobile_number')
    email = data.get('email')
    updated_by = data.get('updated_by')

    staff, error = StaffService.update_staff(staff_id, name, role, mobile_number, email, updated_by)
    if error:
        return jsonify({"error": error}), 400

    return jsonify({"message": "Staff member updated successfully", "staff_id": staff.staff_id}), 200


@staff_bp.route('/<int:staff_id>', methods=['GET'])
def get_staff(staff_id):
    try:
        staff = StaffService.get_staff_by_id(staff_id)

        if not staff:
            return jsonify({"error": "Staff member not found."}), 404

        staff_data = {
            "staff_id": staff.staff_id,
            "name": staff.name,
            "role": staff.role,
            "mobile_number": staff.mobile_number,
            "email": staff.email,
            "created_by": staff.created_by,
            "created_date": staff.created_date.isoformat(),
            "updated_by": staff.updated_by,
            "updated_date": staff.updated_date.isoformat() if staff.updated_date else None
        }

        return jsonify(staff_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@staff_bp.route('/', methods=['GET'])
def get_staff_list():
    try:
        staff_list = StaffService.get_all_staff()

        if not staff_list:
            return jsonify({"error": "No staff details found."}), 404

        staff_data = []
        for staff in staff_list:
            staff_data.append({
                "staff_id": staff.staff_id,
                "name": staff.name,
                "role": staff.role,
                "mobile_number": staff.mobile_number,
                "email": staff.email,
                "created_by": staff.created_by,
                "created_date": staff.created_date.isoformat(),
                "updated_by": staff.updated_by,
                "updated_date": staff.updated_date.isoformat() if staff.updated_date else None
            })

        return jsonify(staff_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
