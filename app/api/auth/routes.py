from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.utils import roles_required
from app.services.auth_service import AuthService
from app.schemas.auth_schema import AuthSchema
from app.errors import DetailedErrorResponse
from . import auth_bp

auth_service = AuthService()


@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        errors = AuthSchema.validate_input(data)

        if errors:
            raise  DetailedErrorResponse(400, "Validation Error", errors)

        username = data.get('username')
        password = data.get('password')
        return auth_service.login_user(username, password)
    except DetailedErrorResponse as error:
        return error.response, error.code
    except Exception as e:
        return DetailedErrorResponse(500, "Unexpected Error", str(e)).response, 500


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # JWT tokens are stateless, so logout is usually handled client-side by simply removing the token.
    return jsonify({"message": "Logged out successfully"}), 200


@auth_bp.route('/reset/<int:loggin_id>', methods=['PUT'])
@roles_required('admin')
def reset_user(loggin_id):
    try:
        message, error = auth_service.reset_user(loggin_id)
        if error:
            raise DetailedErrorResponse(400, "Validation Error", error)
        return jsonify({"message": message}), 200
    except DetailedErrorResponse as error:
        return error.response, error.code
    except Exception as e:
        return DetailedErrorResponse(500, "Unexpected Error", str(e)).response, 500
