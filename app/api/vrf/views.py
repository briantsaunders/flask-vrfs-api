# import third party libs
from flask_apispec.annotations import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource

# import app libs
from app.api import api
from app.api.errors import error_response
from app.core.vrf_operations import VrfOperations
from app.schemas.response.vrf import VrfResponseSchema
from app.schemas.query.vrfs import VrfsQuerySchema
from app.schemas.validations import Validations


@doc(tags=["vrfs"])
class Vrf(MethodResource):
    @marshal_with(VrfResponseSchema)
    def get(self, vrf_id):
        try:
            Validations().validate_vrf(vrf_id)
        except:
            return error_response(400, message=f"{vrf_id} is invalid")
        return VrfOperations().get_vrf(vrf_id)

    def delete(self, vrf_id):
        try:
            Validations().validate_vrf(vrf_id)
        except:
            return error_response(400, message=f"{vrf_id} is invalid")
        VrfOperations().delete_vrf(vrf_id)
        return {}


vrf_view = Vrf.as_view("vrf")
api.add_url_rule("/vrfs/<int:vrf_id>", view_func=vrf_view)
