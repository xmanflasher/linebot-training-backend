from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()


class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    join_code = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
