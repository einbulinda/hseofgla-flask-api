from flask import current_app
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
    def update_product(product_id, product_data):
        """
        Update product details and all its relations for attributes, variants and inventory.
        :param product_id: ID of the product to be updated
        :param product_data: Dictionary containing the product and related data
        :return: Updated product and an optional error message.
        """

        try:
            # Start a transaction
            with db.session.begin():
                # 1. Fetch the Product
                product = Product.query.get(product_id)
                if not product:
                    return None, "Product not found."

                # 2. Update Product Details
                if 'product_name' in product_data:
                    product.product_name = product_data['product_name']

                if 'category_id' in product_data:
                    product.category_id = product_data['category_id']

                if 'is_active' in product_data:
                    product.is_active = product_data['is_active']
                product.updated_by = product_data['updated_by']

                db.session.flush()

                # 3. Update Variants
                if 'variants' in product_data:
                    for variant_data in product_data['variants']:
                        variant_id = variant_data.get('variant_id')

                        if variant_id:
                            # Update Existing Variant
                            variant = ProductVariants.query.get(variant_id)
                            if not variant:
                                return None, f' Variant with ID {variant_id} not found'
                            if 'price' in variant_data:
                                variant.price = variant_data['price']
                            if 'sku' in variant_data:
                                variant.sku = variant_data['price']
                            variant.updated_by = product_data['updated_by']
                        else:
                            # Add New Variant
                            new_variant = ProductVariants(
                                product_id=product_id,
                                price=variant_data['price'],
                                sku=variant_data['sku'],
                                created_by=product_data['updated_by']
                            )
                            db.session.add(new_variant)
                            db.session.flush()

                        # Step 4: Update or Add Product Attributes
                        if 'attributes' in variant_data:
                            for attribute_data in variant_data['attributes']:
                                attribute_id = attribute_data.get('attribute_id')

                                if attribute_id:
                                    attribute = ProductAttributes.query.get(attribute_id)

                                    if not attribute:
                                        return None, f'Attribute with ID: {attribute_id} not found.'

                                    if 'name' in attribute_data:
                                        attribute.name = attribute_data['name']
                                    if 'value' in attribute_data:
                                        attribute.value = attribute_data['value']
                                    attribute.updated_by = product_data['updated_by']
                                else:
                                    new_attribute = ProductVariants(
                                        variant_id=variant_id or new_variant.variant_id,
                                        name=attribute_data['name'],
                                        value=attribute_data['value'],
                                        created_by=product_data['updated_by']
                                    )
                                    db.session.add(new_attribute)
                                    db.session.flush()

                        # Step 5: Update or Add Inventory
                        if 'inventory' in variant_data:
                            inventory_data = variant_data['inventory']
                            inventory = Inventory.query.filter_by(variant_id=variant_id).first()

                            if inventory:
                                inventory.quantity = inventory_data.get('quantity', inventory.quantity)
                                inventory.warehouse_stock = inventory_data.get('warehouse_stock', inventory.warehouse_stock)
                                inventory.shop_stock = inventory_data.get('shop_stock', inventory.shop_stock)
                                inventory.reorder_level = inventory_data.get('reorder_level', inventory.reorder_level)
                                inventory.updated_by = product_data['updated_by']
                            else:
                                new_inventory = Inventory(
                                    variant_id=variant_id or new_variant.variant_id,
                                    quantity=inventory_data.get('quantity', 0),
                                    warehouse_stock=inventory_data.get('warehouse_stock', 0),
                                    shop_stock=inventory_data.get('shop_stock', 0),
                                    reorder_level=inventory_data.get('reorder_level', 0),
                                    created_by=product_data.get('created_by')
                                )
                                db.session.add(new_inventory)
                                db.session.flush()
            # Commit the transaction
            db.session.commit()

            return product, None

        except SQLAlchemyError as e:
            # Rollback transaction in case of an error
            db.session.rollback()
            return None, f'An error has occurred: {str(e)}'

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
    def get_products():
        try:
            products = Product.query.all()
            product_list = [product.to_dict() for product in products]
            return product_list, None
        except SQLAlchemyError as e:
            return None, str(e)
