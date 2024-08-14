from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db
from app.models.login_details import LoginDetails
from app.models.staff import Staff


class StaffService:

    @staticmethod
    def create_staff(name, role, mobile_number=None, email=None, username=None, password=None, created_by=None):
        """
        Create a new staff and their login details
        :param name: Name of the staff member
        :param role: Role of the staff member
        :param mobile_number: Contact of staff member
        :param email: Email address of staff member
        :param username: Username for login
        :param password: Password for login
        :param created_by: ID of the staff who is creating this member
        :return: Newly created staff member and an optional error message
        """
        try:
            # Check if email or username already exists
            if email and Staff.query.filter_by(email=email).first():
                return None, "Email already exists with another user."

            if username and LoginDetails.query.filter_by(username=username).first():
                return None, "Username already taken."

            # Start a transaction
            with db.session.begin():
                # Create the staff
                new_staff = Staff(
                    name=name,
                    role=role,
                    mobile_number=mobile_number,
                    email=email,
                    created_by=created_by
                )

                db.session.add(new_staff)
                db.session.flush()  # Avail staff_id for next operation.

                # Create the login details
                if username and password:
                    hashed_password = generate_password_hash(password)
                    login_details = LoginDetails(
                        staff_id=new_staff.staff_id,
                        username=username,
                        password=hashed_password,
                        created_by=created_by
                    )
                    db.session.add(login_details)

            # Commit the transaction
            db.session.commit()
            return new_staff, None

        except SQLAlchemyError as e:
            # Rollback transaction in case of an error
            db.session.rollback()
            return None, f"An error occurred: {str(e)}"

    @staticmethod
    def update_staff(staff_id, name=None, role=None, mobile_number=None, email=None, username=None, password=None, updated_by=None):
        """
        Update an existing staff member and/or their login details.
        :param staff_id:
        :param name:
        :param role:
        :param mobile_number:
        :param email:
        :param username:
        :param password:
        :param updated_by:
        :return:
        """
        pass

    @staticmethod
    def get_staff_by_id(staff_id):
        """
        Retrieve a staff member by their 'ID'
        :param staff_id: 'ID' of the staff member
        :return: The staff member object or none if not found.
        """
        return Staff.query.get(staff_id)

    @staticmethod
    def get_all_staff():
        """
        Retrieve all staff members.
        :return: A list of all staff members.
        """
        return Staff.query.all()

    @staticmethod
    def delete_staff(staff_id):
        pass
