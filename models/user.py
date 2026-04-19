from .database import db
from .user_team import UserTeam

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(50), unique=True, nullable=False)
    display_name = db.Column(db.String(100))
    # 多對多關係
    user_teams = db.relationship("UserTeam", back_populates="user", cascade="all, delete-orphan")
    
    # 認證與付費等級
    subscription = db.Column(db.String(20), default="Basic")  # Basic or Premium
    role = db.Column(db.String(20), default="member")  # 個人基礎預設角色
    
    # New fields from frontend mock
    gender = db.Column(db.String(10))
    character = db.Column(db.String(20))
    picture_url = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
