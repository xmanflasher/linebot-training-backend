# firebase/firebase_init.py
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()

cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")  # .env中設定的 JSON 路徑
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# 避免重複初始化
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()
