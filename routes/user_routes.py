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
        "subscription": user.subscription,
        "team_ids": [ut.team_id for ut in user.user_teams]
    })
