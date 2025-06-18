from flask import Flask
from flask_cors import CORS
from config import MODE
from routes.linebot_routes import linebot_bp
from routes.test_routes import test_bp

app = Flask(__name__)
CORS(app)  # 允許前端請求


@app.route("/")
def index():
    return "Backend Running"


# 根據 mode 載入不同的 route
if MODE == "development":
    app.register_blueprint(test_bp)  # 測試 API
if MODE in ["development", "production"]:
    app.register_blueprint(linebot_bp)  # 正式 LINE Bot webhook

    # if __name__ == "__main__":
    #     app.run(debug=(MODE == "development"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
