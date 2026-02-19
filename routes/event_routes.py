from flask import Blueprint, jsonify
from models.event import Event

event_bp = Blueprint("event_bp", __name__)

@event_bp.route("/events", methods=["GET"])
def get_events():
    events = Event.query.order_by(Event.date).all()
    return jsonify([event.to_dict() for event in events])

@event_bp.route("/events/<event_id>", methods=["GET"])
def get_event_detail(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({"message": "Event not found"}), 404
    return jsonify(event.to_dict())
