from marshmallow import fields, validate, Schema, ValidationError


class ProductAttributeSchema(Schema):
    name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=50, error="Attribute name must be between 1 and 50 characters.")
    )
    value = fields.String(
        required=True,
        validate=validate.Length(min=1, max=50, error="Attribute value must be between 1 and 50 characters.")
    )


class InventorySchema(Schema):
    quantity = fields.Integer(
        required=True,
        validate=validate.Range(min=0, error="Quantity cannot be negative.")
    )
    warehouse_stock = fields.Integer(
        required=False,
        validate=validate.Range(min=0, error="Warehouse stock cannot be negative."),
        default=0
    )
    shop_stock = fields.Integer(
        required=False,
        validate=validate.Range(min=0, error="Shop stock cannot be negative."),
        default=0
    )
    reorder_level = fields.Integer(
        required=False,
        validate=validate.Range(min=0, error="Reorder level cannot be negative."),
        default=0
    )


class ProductVariantSchema(Schema):
    variant_id = fields.Integer(dump_only=True)
    sku = fields.String(
        required=True,
        validate=validate.Length(min=1, max=255, error="SKU must be between 1 and 255 characters.")
    )
    price = fields.Decimal(
        required=True,
        validate=validate.Range(min=0, error="Price must be greater than or equal to 0.")
    )
    attributes = fields.List(fields.Nested(ProductAttributeSchema), required=False)
    inventory = fields.Nested(InventorySchema, required=False)


class ProductSchema(Schema):
    product_id = fields.Integer(dump_only=True)
    product_name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=255, error="Product name must be between 1 and 255 characters.")
    )
    category_id = fields.Integer(
        required=True,
        validate=validate.Range(min=1, error="Category ID must be a positive integer.")
    )
    is_active = fields.Boolean(required=False, default=True)
    created_by = fields.Integer(dump_only=True)
    created_date = fields.DateTime(dump_only=True)
    updated_by = fields.Integer(dump_only=True)
    updated_date = fields.DateTime(dump_only=True)
    variants = fields.List(fields.Nested(ProductVariantSchema), required=False)

    @staticmethod
    def validate_input(data):
        """
        Validates the input data against the schema.
        :param data: Dict containing the input fields.
        :return: None if valid, or validation errors as a dictionary.
        """
        schema = ProductSchema()
        try:
            schema.load(data)
            return None
        except ValidationError as err:
            return err.messages
