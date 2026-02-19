from app import app
from models.database import db
from models.user import User
from models.team import Team
from models.event import Event
from utils.mock_data import init_mock_data

def verify():
    with app.app_context():
        print("Running init_mock_data()...")
        try:
            init_mock_data()
        except Exception as e:
            print(f"FAILED: init_mock_data raised exception: {e}")
            return

        print("\nVerifying data counts...")
        
        user_count = User.query.count()
        team_count = Team.query.count()
        event_count = Event.query.count()

        print(f"Users: {user_count}")
        print(f"Teams: {team_count}")
        print(f"Events: {event_count}")

        # Assertions
        assert user_count > 0, "User count should be > 0"
        assert team_count == 3, f"Team count should be 3, got {team_count}"
        assert event_count == 4, f"Event count should be 4, got {event_count}"

        # Sample check
        event = Event.query.filter_by(id='mock1').first()
        assert event is not None, "Event mock1 not found"
        assert event.title == '模擬練習 - 河濱公園', f"Event title mismatch, got {event.title}"
        
        print("\nSUCCESS: Data verification passed!")

if __name__ == "__main__":
    verify()
