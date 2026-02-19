# routes/team_routes.py
from flask import Blueprint, request, jsonify
from repositories.team_repository import TeamRepository
from utils.auth import jwt_required, get_current_user

team_bp = Blueprint("team_bp", __name__)


@team_bp.route("/teams/create", methods=["POST"])
@jwt_required()
def create_team():
    data = request.get_json()
    user = get_current_user()

    if user.team_id:
        return jsonify({"message": "已加入團隊"}), 400

    team = TeamRepository.create(name=data["name"])
    
    # Update user - since User model is imported in TeamRepository but not here for mutation, 
    # we might need UserRepository or just update the object.
    # To keep it consistent, let's use UserRepository later or just update the user object.
    from models.database import db
    user.team_id = team.id
    user.role = "admin"
    db.session.commit()
    
    return jsonify({"message": "團隊已創建"})


@team_bp.route("/teams/<team_id>/join", methods=["POST"])
@jwt_required()
def join_team(team_id):
    user = get_current_user()
    if user.team_id:
        return jsonify({"message": "已加入團隊"}), 400

    team = TeamRepository.get_by_id(team_id)
    if not team:
        return jsonify({"message": "團隊不存在"}), 404

    from models.database import db
    user.team_id = team.id
    user.role = "member"
    db.session.commit()
    return jsonify({"message": "已加入團隊"})


@team_bp.route("/teams", methods=["GET"])
def get_all_teams():
    teams = TeamRepository.get_all()
    result = []
    for t in teams:
        result.append({
            "id": t.id,
            "name": t.name,
            "location": t.location,
            "description": t.description,
            "is_public": t.is_public,
            "created_at": t.created_at.isoformat() if t.created_at else None
        })
    return jsonify(result)

@team_bp.route("/teams/<team_id>", methods=["GET"])
def get_team_by_id(team_id):
    team = TeamRepository.get_by_id(team_id)
    if not team:
        return jsonify({"message": "團隊不存在"}), 404
    return jsonify({
        "id": team.id,
        "name": team.name,
        "location": team.location,
        "description": team.description,
        "is_public": team.is_public,
        "created_at": team.created_at.isoformat() if team.created_at else None
    })

@team_bp.route("/teams/search", methods=["GET"])
def search_team():
    invite_code = request.args.get("inviteCode")
    if not invite_code:
        return jsonify({"message": "請提供邀請碼"}), 400
    
    team = TeamRepository.find_by_join_code(invite_code)
    if not team:
        return jsonify(None)
    
    return jsonify({
        "id": team.id,
        "name": team.name,
        "location": team.location,
        "description": team.description,
        "is_public": team.is_public,
        "inviteCode": team.join_code,
        "created_at": team.created_at.isoformat() if team.created_at else None
    })
