from marshmallow import Schema, validate, fields, ValidationError


class StaffSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=3, max=50, error="Name must be between 3 and 50 characters"))
    role = fields.String(required=True, validate=validate.OneOf(["customer", "admin", "staff"], error="Invalid customer role"))
    email = fields.Email(required=True, validate=validate.Email(error="Invalid email format"))
    mobile_number = fields.String(required=True,
                                  validate=validate.Regexp(r'^\+?[1-9]\d{1,14}$', error="Invalid phone number format"))
    created_by = fields.Integer(required=True)

    @staticmethod
    def validate_input(data):
        """
        Validates the input data against the schema.
        :param data: Dict containing the input fields.
        :return: None if valid, or validation errors as a dictionary.
        """
        schema = StaffSchema()
        try:
            schema.load(data)
            return None
        except ValidationError as err:
            return err.messages

