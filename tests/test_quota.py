import pytest
from models.user import User
from models.database import db

def test_basic_user_quota_create(client, auth_header):
    # Setup user
    with client.application.app_context():
        user = User(line_id="test_basic", display_name="Basic User", subscription="Basic")
        db.session.add(user)
        db.session.commit()
        user_id = user.id

    headers = auth_header(user_id)
    
    # 建立第一支隊伍 (應成功)
    resp1 = client.post("/api/teams/create", json={"name": "Team A"}, headers=headers)
    assert resp1.status_code == 200
    
    # 建立第二支隊伍 (應失敗 - 402)
    resp2 = client.post("/api/teams/create", json={"name": "Team B"}, headers=headers)
    assert resp2.status_code == 402
    assert "上限" in resp2.get_json()["message"]

def test_basic_user_quota_join(client, auth_header):
    # Setup teams to join
    with client.application.app_context():
        from models.team import Team
        t1 = Team(name="Public 1")
        t2 = Team(name="Public 2")
        t3 = Team(name="Public 3")
        u = User(line_id="joiner", display_name="Joiner", subscription="Basic")
        db.session.add_all([t1, t2, t3, u])
        db.session.commit()
        team_ids = [t1.id, t2.id, t3.id]
        user_id = u.id

    headers = auth_header(user_id)

    # Join 1
    client.post(f"/api/teams/{team_ids[0]}/join", headers=headers)
    # Join 2
    client.post(f"/api/teams/{team_ids[1]}/join", headers=headers)
    
    # Join 3 (應失敗)
    resp_full = client.post(f"/api/teams/{team_ids[2]}/join", headers=headers)
    assert resp_full.status_code == 402
    assert "上限" in resp_full.get_json()["message"]
