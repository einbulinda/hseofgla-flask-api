from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify, current_app


def staff_required(fn):
    """Authentication decorator to identify user is a staff"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("role").lower() not in ["staff", "admin"]:
                return jsonify({"error": "Access to this resource is forbidden"}), 403
        except RuntimeError as e:
            # To handle cases with no active request contexts
            current_app.logger.error(f"Error required in staff_required decorator: {str(e)}")
            return jsonify({"error": "Authorization failed, no active request context"}), 500
        return fn(*args, **kwargs)
    return wrapper()
