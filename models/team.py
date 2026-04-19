from .database import db
from .user_team import UserTeam
import uuid

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    join_code = db.Column(db.String(10), unique=True, nullable=True)
    location = db.Column(db.String(100))
    description = db.Column(db.String(255))
    is_public = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # 多對多關係
    user_teams = db.relationship("UserTeam", back_populates="team", cascade="all, delete-orphan")
