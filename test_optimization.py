from app import app
import json

def test_mock_auth():
    client = app.test_client()
    
    # 1. Test without Mock Header (should fail on protected route)
    print("Testing protected route without mock header...")
    response = client.post('/api/teams/create', json={"name": "Test Team"})
    assert response.status_code == 401
    print("Correctly denied access without token or mock header.")

    # 2. Test with Mock Header (UID001)
    print("\nTesting protected route with X-Mock-User-ID: UID001...")
    # UID001 (Emma) is initialized in init_mock_data
    response = client.post('/api/teams/create', 
                            json={"name": "Emma's New Team"},
                            headers={"X-Mock-User-ID": "UID001"})
    
    # Note: UID001 already has a team in init_mock_data, so it should return 400 "已加入團隊"
    # unless we use a different user or check the message.
    print(f"Response status: {response.status_code}")
    data = json.loads(response.data)
    print(f"Response message: {data.get('message')}")
    
    if response.status_code == 400 and data.get('message') == "已加入團隊":
        print("Mock Auth successful: User recognized as UID001 (Emma).")
    elif response.status_code == 200:
         print("Mock Auth successful: Team created.")
    else:
        assert False, f"Mock Auth failed with status {response.status_code}"

    # 3. Test Repository Pattern (Get all teams)
    print("\nTesting Repository Pattern (get_all_teams)...")
    response = client.get('/api/teams')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) >= 3
    print(f"Successfully retrieved {len(data)} teams using Repository Pattern.")

    print("\nSUCCESS: Optimization and Mock Auth verified!")

if __name__ == "__main__":
    test_mock_auth()
