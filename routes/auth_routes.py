from flask import Blueprint, request, jsonify
from models.database import db
from models.user import User
from utils.auth import create_access_token
import uuid

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    line_id = data.get("line_id")
    display_name = data.get("display_name")
    picture_url = data.get("picture_url")

    if not line_id:
        return jsonify({"message": "Miss line_id"}), 400

    # Sync User
    user = User.query.filter_by(line_id=line_id).first()
    if not user:
        user = User(
            line_id=line_id,
            display_name=display_name,
            picture_url=picture_url,
            role="member"
        )
        db.session.add(user)
    else:
        # Update user profile
        user.display_name = display_name if display_name else user.display_name
        user.picture_url = picture_url if picture_url else user.picture_url
    
    db.session.commit()

    # Generate JWT
    token = create_access_token(user.id)

    return jsonify({
        "token": token,
        "user_id": user.id,
        "line_id": user.line_id,
        "display_name": user.display_name,
        "role": user.role,
        "team_id": user.team_id
    })
