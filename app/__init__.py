# import third party libs
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_cors import CORS

# import app libs
from config import config


def create_app(config_name=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    register_extensions(app)
    register_blueprints(app)
    register_spec(app)
    return app


def register_extensions(app):
    CORS(app)
    return app


def register_blueprints(app):
    from app.api import api

    app.register_blueprint(api)
    return None


def register_spec(app):
    app.config.update(
        {
            "APISPEC_SPEC": APISpec(
                title="Flask VRFs API",
                version="0.0.1",
                openapi_version="2.0",
                plugins=[MarshmallowPlugin()],
            ),
            "APISPEC_SWAGGER_URL": "/api/docs/apispec.json",
            "APISPEC_SWAGGER_UI_URL": "/api/docs",
        }
    )
    docs = FlaskApiSpec(app)
    from app.api.vrf.views import Vrf

    docs.register(Vrf, blueprint="api")
    from app.api.vrfs.views import Vrfs

    docs.register(Vrfs, blueprint="api")
