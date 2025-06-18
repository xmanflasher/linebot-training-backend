# routes/team_routes.py
from flask import Blueprint, request, jsonify
from models.team import Team, db
from models.user import User
from utils.auth import jwt_required, get_current_user

team_bp = Blueprint("team_bp", __name__)


@team_bp.route("/teams/create", methods=["POST"])
@jwt_required()
def create_team():
    data = request.get_json()
    user = get_current_user()

    if user.team_id:
        return jsonify({"message": "已加入團隊"}), 400

    team = Team(name=data["name"])
    db.session.add(team)
    db.session.flush()
    user.team_id = team.id
    user.role = "admin"
    db.session.commit()
    return jsonify({"message": "團隊已創建"})


@team_bp.route("/teams/<int:team_id>/join", methods=["POST"])
@jwt_required()
def join_team(team_id):
    user = get_current_user()
    if user.team_id:
        return jsonify({"message": "已加入團隊"}), 400

    team = Team.query.get(team_id)
    if not team:
        return jsonify({"message": "團隊不存在"}), 404

    user.team_id = team.id
    user.role = "member"
    db.session.commit()
    return jsonify({"message": "已加入團隊"})


@team_bp.route("/teams/all", methods=["GET"])
def get_all_teams():
    teams = Team.query.all()
    return jsonify([{"id": t.id, "name": t.name} for t in teams])
