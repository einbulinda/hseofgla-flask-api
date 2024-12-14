from flask import request, jsonify
from . import category_bp
from app.utils import roles_required
from app.services import CategoryService
from app.schemas import CategorySchema
from app.errors import DetailedErrorResponse


@category_bp.route('/', methods=['POST'])
def create_category():
    try:
        data = request.get_json()
        errors = CategorySchema.validate_input(data)

        if errors:
            raise DetailedErrorResponse(400, "Validation Error", errors)

        new_category = CategoryService.create_category(
            category_name=data.get('category_name'),
            created_by=data.get('created_by'),
            parent_category_id=data.get('parent_category_id')
        )
        return jsonify(new_category.to_dict()), 201

    except DetailedErrorResponse as error:
        return error.response, error.code
    except Exception as e:
        return DetailedErrorResponse(500, "Unexpected Error", str(e)).response, 500


@category_bp.route('/<int:category_id>', methods=['PUT'])
@roles_required('admin')
def update_category(category_id):
    try:
        data = request.get_json()
        errors = CategorySchema.validate_input(data)

        if errors:
            raise DetailedErrorResponse(400, "Validation Error", errors)

        category_name = data.get('category_name')
        updated_by = data.get('updated_by')
        parent_category_id = data.get('parent_category_id')

        category = CategoryService.update_category(category_id, category_name, updated_by, parent_category_id)
        return jsonify(category.to_dict()), 200

    except DetailedErrorResponse as error:
        return error.response, error.code
    except Exception as e:
        return DetailedErrorResponse(500, "Unexpected Error", str(e)).response, 500


@category_bp.route('/', methods=['GET'])
@roles_required('admin')
def get_all_categories():
    try:
        categories = CategoryService.get_all_categories()
        return jsonify({"data": category.to_dict() for category in categories}), 200
    except DetailedErrorResponse as error:
        return error.response, error.code
    except Exception as e:
        # Catch any unexpected errors with a generic error message
        return DetailedErrorResponse(500, "Unexpected Error", str(e)).response, 500


@category_bp.route('/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    try:
        category = CategoryService.get_category_by_id(category_id)
        return jsonify({"data": category.to_dict()}), 200
    except DetailedErrorResponse as error:
        return error.response, error.code
    except Exception as e:
        return DetailedErrorResponse(500, "Unexpected Error", str(e)).response, 500
