from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify


def roles_required(*roles):
    """
    Authenticates if the user has necessary access credentials for the resource
    :param roles: Provide the role expected for the resource
    :return: Grants permission based on role provided
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()

            # Check is user role matches required role
            user_role = claims.get('role')
            if user_role not in roles:
                return jsonify({"error": "Access forbidden: Insufficient privileges"}), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator
