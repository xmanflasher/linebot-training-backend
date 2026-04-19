# from flask import Blueprint, request, jsonify

# test_bp = Blueprint("test", __name__)

# @test_bp.route("/test", methods=["POST"])
# def test_post():
#     data = request.json
#     print("✅ 收到資料：", data)
#     return jsonify({"status": "ok", "data": data}), 200

# routes/test_routes.py
from flask import Blueprint, jsonify
from firebase.firebase_init import db

test_bp = Blueprint("test", __name__)


@test_bp.route("/test/firestore", methods=["GET"])
def test_firestore():
    doc_ref = db.collection("test_collection").document("hello")
    doc_ref.set({"message": "你好，Firestore！"})

    doc = doc_ref.get()
    return jsonify(doc.to_dict())
