from marshmallow import Schema, fields, validate, ValidationError


class CategorySchema(Schema):
    category_name = fields.String(required=True, validate=validate.Length(min=3, max=25))
    parent_category_id = fields.Integer(required=True)
    created_by = fields.Integer(required=True)

    @staticmethod
    def validate_input(data):
        schema = CategorySchema()
        try:
            schema.load(data)
            return None
        except ValidationError as err:
            return err.messages
