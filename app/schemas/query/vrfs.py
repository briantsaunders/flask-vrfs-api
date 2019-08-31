# import third party libs
from marshmallow import Schema, fields, validate

# import app libs
from ..validations import Validations


class VrfsQuerySchema(Schema):
    name = fields.String(required=True, validate=Validations().validate_vrf_name)
    table = fields.Integer(required=True, validate=Validations().validate_vrf_table)

    class Meta:
        strict = True
