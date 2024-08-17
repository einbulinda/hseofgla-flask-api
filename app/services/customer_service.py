from app.models import LoginDetails, Customer
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db
from flask import current_app


class CustomerService:
    @staticmethod
    def register_customer(name, mobile_number, email, created_by, username, password):
        """
        Create a new customer with login credentials
        :param name: Customers preferred name
        :param mobile_number: Primary contact mobile number
        :param email: Primary email address for customer
        :param created_by: User ID creating the customer
        :param username: username for log in to the system
        :param password: provided password by customer
        :return: Newly created customer and an optional error message.
        """
        try:
            # Check if email or username exists
            if email and Customer.query.filter_by(email=email).first():
                return None, "Email already exists with another user."

            if username and LoginDetails.query.filter_by(username=username).first():
                return None, "Username already taken."

            # Start of transaction
            new_customer = Customer(
                name=name,
                email=email,
                mobile_number=mobile_number,
                created_by=created_by
            )

            db.session.add(new_customer)
            db.session.flush()

            # Saving login details
            if username and password:
                hashed_password = generate_password_hash(password)
                login_details = LoginDetails(
                    customer_id=new_customer.customer_id,
                    username=username,
                    password=hashed_password,
                    created_by=created_by
                )
                db.session.add(login_details)

            db.session.commit()
            return new_customer, None

        except SQLAlchemyError as e:
            # Rollback transaction on exception
            db.session.rollback()
            return None, f"An error occurred: {str(e)}"

    @staticmethod
    def get_customer_by_id(customer_id):
        """
        Retrieve a customer member by their 'ID'
        :param customer_id: 'ID' of the customer
        :return: The object of customer or none if not found.
        """
        return Customer.query.get(customer_id)

    @staticmethod
    def get_all_customers():
        """Retrieve all customers"""
        return Customer.query.all()

    @staticmethod
    def get_customer_by_email(email):
        """Retrieve customer by email"""
        return Customer.query.filter_by(email=email).first()

    @staticmethod
    def update_customer(customer_id, **kwargs):
        """Updates an existing customer profile
        :param customer_id: ID of customer being updated
        :**kwargs: Customer details being modified
        :return: Updated customer record and an optional error message.
        """
        try:
            # Fetch the record to be updated
            customer = CustomerService.get_customer_by_id(customer_id)
            if not customer:
                return None, f"Customer with the provided details not found."

            # Check if email is being updated
            new_email = kwargs.get('email')
            if new_email and new_email != customer.email:
                existing_email = CustomerService.get_customer_by_email(new_email)
                if existing_email:
                    raise ValueError("The email is already in use by another user.")

            # Update fields
            for key, value in kwargs.items():
                if hasattr(customer, key):
                    setattr(customer, key, value)

            customer.updated_by = kwargs.get('updated_by', customer.updated_by)
            db.session.commit()
            return customer, None

        except SQLAlchemyError as e:
            db.session.rollback()
            return None, f"An error occurred: {str(e)}"
