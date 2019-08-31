# import third party libs
from flask_apispec.annotations import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource

# import app libs
from app.api import api
from app.core.vrf_operations import VrfOperations
from app.schemas.response.vrf import VrfResponseSchema
from app.schemas.query.vrfs import VrfsQuerySchema


@doc(tags=["vrfs"])
class Vrfs(MethodResource):
    @marshal_with(VrfResponseSchema(many=True))
    def get(self):
        return VrfOperations().get_vrfs()

    @use_kwargs(VrfsQuerySchema, locations=["query"])
    @marshal_with(VrfResponseSchema)
    def post(self, **kwargs):
        return VrfOperations().create_vrf(kwargs)


vrfs_view = Vrfs.as_view("vrfs")
api.add_url_rule("/vrfs", view_func=vrfs_view)
