from flask import jsonify, request
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required
from app.extensions import db
from . import auth_bp
from app.models import LoginDetails, Staff

MAX_FAILED_ATTEMPTS = 5


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = LoginDetails.query.filter_by(username=username).first()

    if not user:
        return jsonify({"error": "Invalid username or password"}), 401

    if user.is_locked:
        return jsonify({"error": "Account is locked!"}), 403

    if not check_password_hash(user.password, password):
        user.failed_attempts += 1
        if user.failed_attempts >= MAX_FAILED_ATTEMPTS:
            user.is_locked = True
        db.session.commit()
        return jsonify({"error": "Invalid username or password"}), 401

    # Reset Failed attempts on successful login
    user.failed_attempts = 0
    db.session.commit()

    if user.staff_id:
        user_id = f"staff: {user.staff_id}"
        staff = Staff.query.filter_by(staff_id=user.staff_id).first()
        role = staff.role.lower()
    else:
        user_id = f"customer: {user.customer_id}"
        role = "customer"
    access_token = create_access_token(identity=user_id, additional_claims={"role": role})
    return jsonify({"access_token": access_token}), 200


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # JWT tokens are stateless, so logout is usually handled client-side by simply removing the token.
    return jsonify({"message": "Logged out successfully"}), 200
