from sqlalchemy.exc import SQLAlchemyError
from app.models import Discount
from app.extensions import db


class DiscountService:
    @staticmethod
    def create_discount(discount_data):
        """
        Adds a product discount promotion for specified campaign period
        :param discount_data: Dictionary of the discount details
        :return: Newly created discount parameters and an optional error message
        """
        try:
            new_discount = Discount(
                discount_name=discount_data.get('discount_name'),
                product_id=discount_data.get('product_id'),
                variant_id=discount_data.get('variant_id'),
                discount_rate=discount_data.get('discount_rate'),
                discount_amount=discount_data.get('discount_amount'),
                start_date=discount_data.get('start_date'),
                expiry_date=discount_data.get('expiry_date'),
                description=discount_data.get('description'),
                created_by=discount_data.get('created_by')
            )
            db.session.add(new_discount)
            db.session.commit()
            return new_discount, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, f'An error has occurred while creating a discount: {str(e)}'

    @staticmethod
    def get_discount(discount_id):
        try:
            discount = Discount.query.get(discount_id)
            if not discount:
                return None, "Discount not found."
            return discount, None
        except SQLAlchemyError as e:
            return None, f'An error has occurred while getting discount details: {str(e)}'

    @staticmethod
    def get_discounts():
        try:
            discounts = Discount.query.all()
            return discounts, None
        except SQLAlchemyError as e:
            return None, f'An error has occurred while getting discounts: {str(e)}'

    @staticmethod
    def update_discount(discount_id, update_data):
        """
        Updates an existing discount with the provided update data.

        :param discount_id: The ID of the discount to be updated.
        :param update_data: A dictionary containing the fields and values to update.
        :return: The updated discount object and any error message if encountered.
        """
        try:
            discount = Discount.query.filter_by(discount_id=discount_id).first()
            if not discount:
                return None, "Discount not found."
            # Update Discount Fields:
            discount.discount_name = update_data.get('discount_name', discount.discount_name)
            discount.product_id = update_data.get('product_id', discount.product_id)
            discount.variant_id = update_data.get('variant_id', discount.variant_id)
            discount.discount_rate = update_data.get('discount_rate', discount.discount_rate)
            discount.discount_amount = update_data.get('discount_amount', discount.discount_amount)
            discount.start_date = update_data.get('start_date', discount.start_date)
            discount.expiry_date = update_data.get('expiry_date', discount.expiry_date)
            discount.description = update_data.get('description', discount.description)
            discount.updated_by = update_data.get('updated_by', discount.updated_by)
            discount.updated_date = db.func.current_timestamp()

            db.session.commit()
            return discount, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, f'An error has occurred while updating discount: {str(e)}'

