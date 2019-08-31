# import third party libs
from marshmallow import Schema, fields


class VrfResponseSchema(Schema):
    name = fields.String()
    table = fields.Integer()
    vrf_id = fields.Integer()
