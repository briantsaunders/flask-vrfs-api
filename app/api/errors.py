# import third party libs
from flask import jsonify

# import app libs
from app.api import api


def error_response(status_code, message=None):
    payload = {}
    if message:
        payload["error"] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


@api.errorhandler(422)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"error": messages}), err.code, headers
    else:
        return jsonify({"error": messages}), err.code
