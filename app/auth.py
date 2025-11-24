import os
from functools import wraps
from flask import request, abort

API_KEY = os.getenv("API_KEY")

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get("x-api-key")
        if key != API_KEY:
            abort(401, "Unauthorized")
        return f(*args, **kwargs)
    return decorated