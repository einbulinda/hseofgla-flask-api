from sqlalchemy.exc import SQLAlchemyError
from app.models import Category, Staff
from app.extensions import db
from flask import jsonify
import logging


class CategoryService:

    @staticmethod
    def create_category(category_name, created_by, parent_category_id=None):
        try:
            # Check if the category already exists
            category_exists = Category.query.filter_by(category_name=category_name.lower()).first()
            if category_exists:
                return None, "Category already exists."

            # Create new category
            new_category = Category(
                category_name=category_name.lower(),
                parent_category_id=parent_category_id,
                created_by=created_by
            )
            db.session.add(new_category)
            db.session.commit()
            logging.info("Category created successfully")

            return new_category, None
        except SQLAlchemyError as e:
            db.session.rollback()
            logging.error(e)
            return None, f'An error has occurred: {str(e)}'

    @staticmethod
    def get_category_by_id(category_id):
        try:
            category = Category.query.get(category_id)
            if not category:
                return None, "Category not found."
            return category, None
        except SQLAlchemyError as e:
            return None, f'An error has occurred: {str(e)}'

    @staticmethod
    def update_category(category_id, category_name=None, updated_by=None, parent_category_id=None):
        try:
            category = Category.query.get(category_id)
            if not category:
                return None, "Category not found."

            if category_name:
                category_exists = Category.query.filter_by(category_name=category_name.lower()).first()
                if category_exists and category_exists.category_id != category_id:
                    return None, "Category name already exists."

                category.category_name = category_name

            if parent_category_id is not None:
                if parent_category_id == category_id:
                    return None, "A category cannot be its own parent."
                category.parent_category_id = parent_category_id

            if updated_by:
                category.updated_by = updated_by

            db.session.commit()
            return category, None
        
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, f'An error has occurred: {str(e)}'

    @staticmethod
    def get_all_categories():
        try:
            categories = Category.query.all()
            return categories, None
        except SQLAlchemyError as e:
            return None, f'An error has occurred: {str(e)}'
