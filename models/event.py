from .database import db
import uuid

class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    type = db.Column(db.String(50))
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100))
    participants = db.Column(db.String(255)) # Storing as comma-separated string for simplicity based on mock data
    group_name = db.Column(db.String(50)) # 'group' is a reserved keyword in some SQL, using group_name
    weather = db.Column(db.String(100))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "title": self.title,
            "date": self.date.isoformat() if self.date else None,
            "location": self.location,
            "participants": self.participants,
            "group": self.group_name,
            "weather": self.weather,
            "notes": self.notes,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
