from .database import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(50), unique=True, nullable=False)
    display_name = db.Column(db.String(100))
    team_id = db.Column(db.String(36), db.ForeignKey("teams.id"))
    role = db.Column(db.String(20), default="member")  # 或 'admin'
    
    # New fields from frontend mock
    gender = db.Column(db.String(10))
    character = db.Column(db.String(20))
    picture_url = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
