from models.user_team import UserTeam
from models.user import User

def check_user_quota(user, action_type="join"):
    """
    action_type: 'join' or 'create'
    免費版 (Basic): 
    - 限制加入總隊伍數 < 2
    - 限制管理總隊伍數 < 1
    """
    if user.subscription == "Premium":
        return True, ""

    # 計算當前加入的隊伍數
    joined_teams_count = len(user.user_teams)
    # 計算當前管理的隊伍數 (role='coach' 或 'admin')
    managed_teams_count = sum(1 for ut in user.user_teams if ut.role in ["coach", "admin"])

    if action_type == "join":
        if joined_teams_count >= 2:
            return False, "已達到免費版加入隊伍上限 (2 隊)"
    elif action_type == "create":
        if managed_teams_count >= 1:
            return False, "已達到免費版管理隊伍上限 (1 隊)"
            
    return True, ""
