from app import app
import json

def verify_api():
    client = app.test_client()
    
    # 1. Verify Teams
    print("Testing /api/teams/all ...")
    response = client.get('/api/teams/all')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 3
    print(f"Teams count: {len(data)}")
    # Check fields
    team = data[0]
    assert "description" in team
    assert "location" in team
    assert "created_at" in team
    print("Teams API check passed.")

    # 2. Verify Events
    print("\nTesting /api/events ...")
    response = client.get('/api/events')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 4
    print(f"Events count: {len(data)}")
    # Check fields
    event = data[0]
    assert "type" in event
    assert "title" in event
    assert "date" in event
    print("Events API check passed.")

    # 3. Verify User Profile
    print("\nTesting /api/users/UID001 ...")
    response = client.get('/api/users/UID001')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['line_id'] == 'UID001'
    assert "gender" in data
    assert "character" in data
    assert data['gender'] == '女'
    print("User API check passed.")

    print("\nSUCCESS: All API endpoints verified!")

if __name__ == "__main__":
    verify_api()
