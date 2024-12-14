from sqlalchemy.exc import SQLAlchemyError
from app.errors import DetailedErrorResponse
from app.models import Category
from app.extensions import db


class CategoryService:
    @staticmethod
    def create_category(category_name, created_by, parent_category_id=None):
        try:
            # Check if the category already exists
            category_exists = Category.query.filter_by(category_name=category_name.lower()).first()
            if category_exists:
                raise DetailedErrorResponse(400, "Validation Error", "Category already exists")

            if parent_category_id:
                parent_category = Category.query.get(parent_category_id)
                if not parent_category:
                    raise DetailedErrorResponse(404, "Not Found", "Main category provided does not exist")

            # Create new category
            new_category = Category(
                category_name=category_name.lower(),
                parent_category_id=parent_category_id,
                created_by=created_by
            )
            db.session.add(new_category)
            db.session.commit()
            return new_category
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DetailedErrorResponse(500, "Database Error", f"An error occurred: {str(e)}")

    @staticmethod
    def get_category_by_id(category_id):
        try:
            category = Category.query.get(category_id)
            if not category:
                raise DetailedErrorResponse(404, "Category Not Found",
                                            f"Category with ID {category_id} does not exist.")
            return category
        except SQLAlchemyError as e:
            raise DetailedErrorResponse(500, "Database Error", f"An error occurred while fetching categories: {str(e)}")

    @staticmethod
    def update_category(category_id, category_name=None, updated_by=None, parent_category_id=None):
        try:
            category = Category.query.get(category_id)
            if not category:
                raise DetailedErrorResponse(404, "Category Not Found",
                                            f"Category with ID {category_id} does not exist.")

            if category_name:
                category_exists = Category.query.filter_by(category_name=category_name.lower()).first()

                if category_exists and category_exists.category_id != category_id:
                    raise DetailedErrorResponse(400, "Bad Request", "Category name already exists.")
                category.category_name = category_name

            if parent_category_id is not None:
                if parent_category_id == category_id:
                    raise DetailedErrorResponse(400, "Bad Request", "A category cannot be its own parent.")
                category.parent_category_id = parent_category_id

            if updated_by:
                category.updated_by = updated_by

            db.session.commit()
            return category

        except SQLAlchemyError as e:
            db.session.rollback()
            raise DetailedErrorResponse(500, "Database Error", f"An error occurred: {str(e)}")

    @staticmethod
    def get_all_categories():
        try:
            categories = Category.query.all()
            if not categories:
                raise DetailedErrorResponse(404, "No Categories Found",
                                            "The application does not have any categories defined.")
            return categories
        except SQLAlchemyError as e:
            raise DetailedErrorResponse(500, "Database Error", f"An error occurred while fetching categories: {str(e)}")
