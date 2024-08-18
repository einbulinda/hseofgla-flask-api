from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.utils import roles_required
from app.services.auth_service import AuthService
from . import auth_bp


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    return AuthService.login_user(username, password)


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # JWT tokens are stateless, so logout is usually handled client-side by simply removing the token.
    return jsonify({"message": "Logged out successfully"}), 200


@auth_bp.route('/reset/<int:loggin_id>', method=['PUT'])
@roles_required('admin')
def reset_user(loggin_id):
    message, error = AuthService.reset_user(loggin_id)
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"message": message}), 200
