from models.database import db
from models.user import User
from models.team import Team
from models.event import Event
from datetime import datetime

def init_mock_data():
    # 由於 Schema 變更，我們先嘗試清空資料
    try:
        db.session.query(User).delete()
        db.session.query(Team).delete()
        db.session.query(Event).delete()
        db.session.commit()
    except Exception as e:
        print(f"Error clearing data (schema mismatch expected if clean run): {e}")
        db.session.rollback()

    print("Initializing mock data from frontend source...")

    # Teams Data (from mockTeamData.js)
    teams = [
        Team(
            id="TEAM001", 
            name="WeekendFighters", 
            join_code="1234",
            location="台北市", 
            description="週末戰士隊，歡迎喜愛運動的你！",
            is_public=True,
            created_at=datetime(2025, 1, 15, 10, 30)
        ),
        Team(
            id="TEAM002", 
            name="CT50+", 
            join_code="5566",
            location="台中市", 
            description="50歲以上的運動愛好者團隊。",
            is_public=True,
            created_at=datetime(2025, 1, 15, 10, 30)
        ),
        Team(
            id="TEAM003", 
            name="TestTeam", 
            join_code="9999",
            location="高雄市", 
            description="測試用的私人小隊。",
            is_public=False,
            created_at=datetime(2025, 1, 15, 10, 30)
        )
    ]

    db.session.add_all(teams)
    db.session.flush()

    # Users Data (from mockProfiles.js)
    users_source = [
        {"id": "UID001", "name": "Emma", "teams": ["TEAM001"], "gender": "女", "char": "DRUM", "role": "admin"},
        {"id": "UID002", "name": "Ray", "teams": ["TEAM001"], "gender": "男", "char": "左", "role": "member"},
        {"id": "UID003", "name": "勇哥", "teams": ["TEAM001"], "gender": "男", "char": "左", "role": "member"},
        {"id": "UID004", "name": "Peter", "teams": ["TEAM001"], "gender": "男", "char": "右", "role": "member"},
        {"id": "UID005", "name": "翔哥", "teams": ["TEAM001"], "gender": "男", "char": "右", "role": "member"},
        {"id": "UID006", "name": "狐狸", "teams": ["TEAM001"], "gender": "男", "char": "右", "role": "member"},
        {"id": "UID007", "name": "Alan", "teams": ["TEAM001", "TEAM002"], "gender": "男", "char": "右", "role": "member"},
        {"id": "UID008", "name": "Roger", "teams": ["TEAM001"], "gender": "男", "char": "左", "role": "member"},
        {"id": "UID009", "name": "DT", "teams": ["TEAM001", "TEAM002"], "gender": "男", "char": "左", "role": "member"},
        {"id": "UID010", "name": "豪哥", "teams": ["TEAM001"], "gender": "男", "char": "左", "role": "member"},
        {"id": "UID011", "name": "輔哥", "teams": ["TEAM001"], "gender": "男", "char": "左", "role": "member"},
        {"id": "UID012", "name": "永哲", "teams": ["TEAM001"], "gender": "男", "char": "右", "role": "member"},
        {"id": "UID013", "name": "顏正福", "teams": ["TEAM001", "TEAM002"], "gender": "男", "char": "左", "role": "member"},
        {"id": "UID014", "name": "陳恩理", "teams": ["TEAM001", "TEAM002"], "gender": "男", "char": "左", "role": "member"},
        {"id": "UID015", "name": "陳東其", "teams": ["TEAM001", "TEAM002"], "gender": "男", "char": "右", "role": "member"},
        {"id": "UID016", "name": "李志剛", "teams": ["TEAM001", "TEAM002"], "gender": "男", "char": "右", "role": "member"},
        {"id": "UID017", "name": "吉路", "teams": ["TEAM001", "TEAM002"], "gender": "男", "char": "右", "role": "member"},
        {"id": "UID018", "name": "殷慕柏", "teams": ["TEAM001", "TEAM002"], "gender": "男", "char": "左", "role": "member"},
        {"id": "UID019", "name": "乃文", "teams": ["TEAM001"], "gender": "男", "char": "右", "role": "member"},
        {"id": "UID020", "name": "momo", "teams": ["TEAM001"], "gender": "男", "char": "COX", "role": "member"},
        {"id": "UID021", "name": "Andy", "teams": ["TEAM001"], "gender": "男", "char": "右", "role": "member"},
        {"id": "UID022", "name": "楊彥博", "teams": ["TEAM001"], "gender": "男", "char": "DRUM", "role": "member"},
        {"id": "UID023", "name": "Eric", "teams": ["TEAM001"], "gender": "男", "char": "COX", "role": "member"},
    ]

    for u in users_source:
        user = User(
            line_id=u["id"],
            display_name=u["name"],
            team_id=u["teams"][0] if u["teams"] else None,
            role=u["role"],
            gender=u["gender"],
            character=u["char"],
            is_active=True
        )
        db.session.add(user)

    # Events Data (from mockEventData.js)
    events = [
        Event(
            id='mock1',
            type='practice',
            title='模擬練習 - 河濱公園',
            date=datetime.fromisoformat('2025-05-05T15:00:00'),
            location='台北市河濱公園',
            participants='Alice,Bob,Charlie',
            group_name='混合組',
            weather='晴時多雲，氣溫 28°C',
            notes='請準時集合，注意補水',
            created_at=datetime.fromisoformat('2025-04-25T10:00:00')
        ),
        Event(
            id='mock2',
            type='match',
            title='模擬比賽 - 碧潭水域',
            date=datetime.fromisoformat('2025-05-05T09:00:00'),
            location='新店碧潭',
            participants='Alice,David,Eva',
            group_name='公開組',
            weather='晴天，氣溫 30°C',
            notes='攜帶比賽裝備，提前報到',
            created_at=datetime.fromisoformat('2025-04-28T14:30:00')
        ),
        Event(
            id='mock3',
            type='practice',
            title='模擬練習 - 大佳河濱',
            date=datetime.fromisoformat('2025-05-05T07:00:00'),
            location='台北大佳河濱',
            participants='Bob,Charlie,Fiona',
            group_name='女子組',
            weather='陰天，氣溫 26°C',
            notes='集合時間為早上6:50',
            created_at=datetime.fromisoformat('2025-04-29T09:15:00')
        ),
        Event(
            id='mock4',
            type='match',
            title='模擬比賽 - 台中港',
            date=datetime.fromisoformat('2025-05-05T13:30:00'),
            location='台中港區',
            participants='George,Helen,Ivy',
            group_name='混合組',
            weather='多雲，氣溫 29°C',
            notes='準備替補名單',
            created_at=datetime.fromisoformat('2025-04-30T11:00:00')
        ),
    ]
    db.session.add_all(events)

    db.session.commit()
    print("Mock data initialized successfully.")
