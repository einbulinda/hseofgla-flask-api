from marshmallow import Schema, fields, validate, ValidationError


def validate_positive_integer(value):
    if value < 0:
        raise ValidationError("Must be a positive integer")


class CategorySchema(Schema):
    category_name = fields.String(required=True, validate=validate.Length(min=3, max=25, error="Category name must be between 3 to 25 characters"))
    parent_category_id = fields.Integer(required=True, validate=validate_positive_integer)
    created_by = fields.Integer(required=True, validate=validate_positive_integer)

    @staticmethod
    def validate_input(data):
        schema = CategorySchema()
        try:
            schema.load(data)
            return None
        except ValidationError as err:
            return err.messages
