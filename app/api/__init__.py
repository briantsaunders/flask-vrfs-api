# import third party libs
from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/api")

from . import vrf
from . import vrfs
