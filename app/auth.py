import os
from functools import wraps
from flask import request, abort

API_KEY = os.getenv("API_KEY")

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not API_KEY:
            abort(500, "Server misconfiguration: API_KEY missing")

        key = request.headers.get("x-api-key")

        if not key:
            abort(401, "API Key required")

        if key != API_KEY:
            abort(401, "Unauthorized")
            
        return f(*args, **kwargs)
    return decorated