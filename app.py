from flask import Flask
from flask_cors import CORS
from config import MODE, SQLALCHEMY_DATABASE_URI, SECRET_KEY
from models.database import db
from routes.linebot_routes import linebot_bp
from routes.team_routes import team_bp
from routes.user_routes import user_bp
from routes.test_routes import test_bp
from routes.event_routes import event_bp
from utils.mock_data import init_mock_data
import os

app = Flask(__name__)
CORS(app) # 允許全域跨域請求，包含 OPTIONS 預檢

# 資料庫配置
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

db.init_app(app)

with app.app_context():
    db.create_all()
    init_mock_data() # 初始化測試資料

@app.route("/")
def index():
    return "Backend Running"

# 根據 mode 載入不同的 route
if MODE == "development":
    app.register_blueprint(test_bp)  # 測試 API
    app.register_blueprint(team_bp, url_prefix="/api")
    app.register_blueprint(user_bp, url_prefix="/api")
    app.register_blueprint(event_bp, url_prefix="/api")
if MODE in ["development", "production"]:
    app.register_blueprint(linebot_bp)  # 正式 LINE Bot webhook

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=(MODE == "development"))
