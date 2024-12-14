from flask import jsonify
from .errors import DetailedErrorResponse


# Handle 404 Errors
def handle_404_error(error):
    return DetailedErrorResponse(404, "Resource not found.",
                                 "The requested endpoint or resource does not exist").response


# Handle 400 errors (Bad Request)
def handle_400_error(error):
    return DetailedErrorResponse(400, "Bad Request", "Invalid input provided. Check the data and try again.").response


# Handle 500 errors (Internal Server Error)
def handle_500_error(error):
    return DetailedErrorResponse(500, "Internal Server Error", "Something went wrong on our end.").response
