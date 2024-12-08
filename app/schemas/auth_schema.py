from marshmallow import Schema, fields, validate, ValidationError


class AuthSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=3, max=255))
    password = fields.String(required=True, validate=validate.Length(min=3, max=50))

    @staticmethod
    def validate_input(data):
        schema = AuthSchema()
        try:
            schema.load(data)
            return None
        except ValidationError as err:
            return err.messages
