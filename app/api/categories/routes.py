from flask import request, jsonify
from . import category_bp
from app.utils import roles_required
from app.services import CategoryService


@category_bp.route('/', methods=['POST'])
def create_category():
    data = request.get_json()
    category, error = CategoryService.create_category(
        category_name=data.get('category_name'),
        created_by=data.get('created_by'),
        parent_category_id=data.get('parent_category_id')
    )
    if error:
        return jsonify({"error": error}), 400

    return jsonify(category.to_dict()), 201


@category_bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    category_name = data.get('category_name')
    updated_by = data.get('updated_by')
    parent_category_id = data.get('parent_category_id')

    category, error = CategoryService.update_category(category_id, category_name, updated_by, parent_category_id)

    if error:
        return jsonify({"error": error}), 400

    return jsonify(category.to_dict()), 200


@category_bp.route('/', methods=['GET'])
def get_all_categories():
    categories, error = CategoryService.get_all_categories()
    if error:
        return jsonify({"error": error}), 400
    return jsonify([category.to_dict() for category in categories]), 200


@category_bp.route('/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    category, error = CategoryService.get_category_by_id(category_id)
    if error:
        return jsonify({"error": error}), 400
    return jsonify(category.to_dict()), 200
