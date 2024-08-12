from flask import jsonify
from . import auth_bp

@auth_bp.route('/login', methods=['POST'])
def login():
    # Simulate a login process
    return jsonify({
        "message": "Login successful!"
    })


@auth_bp.route('/register', methods=['POST'])
def register():
    # Simulate a registration process
    return jsonify({
        "message": "Registration successful!"
    })

