import jwt
import datetime
from functools import wraps
from flask import request, jsonify


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Token" in request.headers:
            token = request.headers["Token"]
        if not token:
            return jsonify({"success": False, "message": "Token is missing"}), 401
        try:
            data = jwt.decode(
                token, "secret key")
        except:
            return jsonify({"success": False, "message": "Token is invalid"}), 401
        return f(data["id"], *args, **kwargs)
    return decorated
