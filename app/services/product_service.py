import logging

from sqlalchemy.exc import SQLAlchemyError
from app.models import Inventory, ProductAttributes, Product, ProductVariants
from app.extensions import db


class ProductService:
    @staticmethod
    def add_product(product_data):
        """
        Add a new product along with its variants, attributes, and inventory details.

        :param product_data: Dict containing product details, variants, attributes, and inventory information
        :return: Newly created product or None, and an optional error message.
        """
        try:
            # Start a transaction 05/09/2024
            with (db.session.begin()):
                # 1. Add Product
                new_product = Product(
                    product_name=product_data.get('product_name'),
                    category_id=product_data.get('category_id'),
                    is_active=product_data.get('is_active', True),
                    created_by=product_data.get('created_by')
                )
                db.session.add(new_product)
                db.session.flush()  # To get the product_id for subsequent relations

                # 2. Add Product Variants and Attributes
                for variant_data in product_data.get('variants', []):
                    # Add Product variants
                    new_variant = ProductVariants(
                        product_id=new_product.product_id,
                        sku=variant_data.get('sku'),
                        price=variant_data.get('price'),
                        created_by=product_data.get('created_by')
                    )
                    db.session.add(new_variant)
                    db.session.flush()  # Get the variant_id for attributes and inventory

                    # Add Product Attributes for each variant
                    for attribute_data in variant_data.get('attributes', []):
                        new_attribute = ProductAttributes(
                            variant_id=new_variant.variant_id,
                            name=attribute_data.get('name'),
                            value=attribute_data.get('value'),
                            created_by=product_data.get('created_by')
                        )
                        db.session.add(new_attribute)

                    # Add Inventory for Each Variant
                    inventory_data = variant_data.get('inventory')
                    if inventory_data:
                        new_inventory = Inventory(
                            variant_id=new_variant.variant_id,
                            quantity=inventory_data.get('quantity', 0),
                            warehouse_stock=inventory_data.get('warehouse_stock', 0),
                            shop_stock=inventory_data.get('shop_stock', 0),
                            reorder_level=inventory_data.get('reorder_level', 0),
                            created_by=product_data.get('created_by')
                        )
                        db.session.add(new_inventory)
            # Commit the transaction
            db.session.commit()
            return new_product, None
        except SQLAlchemyError as e:
            # Rollback on exception
            db.session.rollback()
            return None, f"An error has occurred: {str(e)}"

    @staticmethod
    def get_product(product_id):
        try:
            product = Product.query.get(product_id)
            if not product:
                return None, "Product not found."
            return product, None
        except SQLAlchemyError as e:
            return None, f'An error has occurred: {str(e)}'

    @staticmethod
    def update_product():
        pass

    @staticmethod
    def disable_product():
        pass

    @staticmethod
    def get_products():
        try:
            products = Product.query.all()
            product_list = [product.to_dict() for product in products]
            return product_list, None
        except SQLAlchemyError as e:
            return None, str(e)

