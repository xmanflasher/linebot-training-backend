from flask import Blueprint, request, jsonify

test_bp = Blueprint("test", __name__)

@test_bp.route("/test", methods=["POST"])
def test_post():
    data = request.json
    print("✅ 收到資料：", data)
    return jsonify({"status": "ok", "data": data}), 200