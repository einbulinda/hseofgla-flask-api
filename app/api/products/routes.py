from flask import request, jsonify
from . import product_bp
from app.utils import roles_required
from app.services import ProductService


@product_bp.route('/', methods=['POST'])
@roles_required('admin')
def create_product():
    product_data = request.get_json()
    new_product, error = ProductService.add_product(product_data)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "Product created successfully",
        "product": new_product.to_dict()
    }), 201


@product_bp.route('/', methods=['GET'])
def get_products():
    products, error = ProductService.get_products()

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "Products fetched successfully",
        "products": products
    }), 200


@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product, error = ProductService.get_product(product_id)
    if error:
        return jsonify({"error": error}), 400
    return jsonify(product.to_dict()), 200



