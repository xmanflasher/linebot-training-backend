from .database import db
from datetime import datetime

class UserTeam(db.Model):
    __tablename__ = "user_teams"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    team_id = db.Column(db.String(36), db.ForeignKey("teams.id"), primary_key=True)
    role = db.Column(db.String(20), default="member")  # coach or member
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="user_teams")
    team = db.relationship("Team", back_populates="user_teams")
