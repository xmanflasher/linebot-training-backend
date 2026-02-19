import os
from dotenv import load_dotenv

load_dotenv()

MODE = os.getenv("MODE", "development")
FRONTEND_URL = (
    os.getenv("FRONTEND_URL_DEV")
    if MODE == "development"
    else os.getenv("FRONTEND_URL_PROD")
)
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")

# 安全金鑰與資料庫路徑
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-123")
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'data.db')}"
