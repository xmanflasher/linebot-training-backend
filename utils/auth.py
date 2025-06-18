from functools import wraps
from flask import request, jsonify
import jwt
from config import SECRET_KEY
from models.user import User


def jwt_required():
    def wrapper(fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            token = request.headers.get("Authorization", "").replace("Bearer ", "")
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                user = User.query.get(payload["user_id"])
                if not user:
                    raise Exception("User not found")
                request.user = user
            except Exception as e:
                return jsonify({"message": "未授權"}), 401
            return fn(*args, **kwargs)

        return decorated

    return wrapper


def get_current_user():
    return request.user
