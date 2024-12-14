from flask import jsonify
from werkzeug.exceptions import HTTPException


# Custom class for detailed error responses
class DetailedErrorResponse(HTTPException):
    def __init__(self, code, message, details=None):
        self.code = code
        self.message = message
        self.details = details
        self.response = jsonify({
            "error": {
                "code": code,
                "message": message,
                "details": details
            }
        })
