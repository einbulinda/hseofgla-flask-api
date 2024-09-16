from app.models import LoginDetails, Staff
from app.extensions import db
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token


class AuthService:
    MAX_FAILED_ATTEMPTS = 5

    @staticmethod
    def get_loggin_details(username):
        user = LoginDetails.query.filter_by(username=username).first()

        if not user:
            return jsonify({"error": "Invalid username or password"}), 401

        if user.is_locked:
            return jsonify({"error": "Account is locked!"}), 403

        return user

    def login_user(self, username, password):
        user = AuthService.get_loggin_details(username)

        if isinstance(user, tuple):
            return user

        if not check_password_hash(user.password, password):
            user.failed_attempts += 1
            if user.failed_attempts >= self.MAX_FAILED_ATTEMPTS:
                user.is_locked = True
            db.session.commit()
            return jsonify({"error": "Invalid username or password"}), 401

        # Reset Failed attempts on successful login
        user.failed_attempts = 0
        db.session.commit()

        if user.staff_id:
            user_id = user.staff_id
            staff = Staff.query.filter_by(staff_id=user.staff_id).first()
            role = staff.role.lower()
        else:
            user_id = user.customer_id
            role = "customer"
        access_token = create_access_token(identity=user_id, additional_claims={"role": role})
        return jsonify({"access_token": access_token}), 200

    @staticmethod
    def reset_user(loggin_id):
        try:
            user = LoginDetails.query.filter_by(loggin_id=loggin_id).first()
            if not user:
                return None, f"No user found for provided details"

            user.is_locked = False
            user.failed_attempts = 0

            db.session.commit()
            return f"User reset was successful", None

        except SQLAlchemyError as e:
            db.session.rollback()
            return None, f"An error occurred: {str(e)}"
