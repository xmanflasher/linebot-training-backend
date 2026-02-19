from flask import Blueprint, jsonify
from repositories.user_repository import UserRepository

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users/<userId>", methods=["GET"])
def get_user_profile(userId):
    user = UserRepository.find_by_line_id(userId)
    if not user:
        return jsonify({
            "line_id": userId,
            "display_name": "New User",
            "role": "member",
            "team_id": None
        })
    
    return jsonify({
        "line_id": user.line_id,
        "display_name": user.display_name,
        "role": user.role,
        "team_id": user.team_id,
        "team_ids": [user.team_id] if user.team_id else [],  # 新增：相容前端複數欄位
        "gender": user.gender,
        "character": user.character,
        "picture_url": user.picture_url,
        "is_active": user.is_active
    })
