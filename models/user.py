# models/user.py
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(50), unique=True, nullable=False)
    display_name = db.Column(db.String(100))
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    role = db.Column(db.String(20), default="member")  # 或 'admin'
