import os
from dotenv import load_dotenv

load_dotenv()

MODE = os.getenv("MODE", "production")
FRONTEND_URL = (
    os.getenv("FRONTEND_URL_DEV")
    if MODE == "development"
    else os.getenv("FRONTEND_URL_PROD")
)
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
