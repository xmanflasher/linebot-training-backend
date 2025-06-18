from flask import Blueprint, request, abort
# from linebot.v3 import (
#     WebhookHandler
# )
# from linebot.v3.exceptions import (
#     InvalidSignatureError
# )
# from linebot.v3.messaging import (
#     Configuration,
#     ApiClient,
#     MessagingApi,
#     ReplyMessageRequest,
#     TextMessage
# )
# from linebot.v3.webhooks import (
#     MessageEvent,
#     TextMessageContent
# )
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
from linebot.exceptions import InvalidSignatureError
from config import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET, FRONTEND_URL

linebot_bp = Blueprint("linebot", __name__)

# 初始化 LINE
line_bot_api = LineBotApi('LINE_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('LINE_CHANNEL_SECRET')

group_admins = {}

@linebot_bp.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    user_id = event.source.user_id
    group_id = getattr(event.source, 'group_id', None)

    if text.startswith("/setadmin") and group_id:
        group_admins[group_id] = user_id
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="✅ 你已被設為本群組管理員。"))

    elif text.startswith("/newpractice"):
        if group_id and group_admins.get(group_id) == user_id:
            liff_url = f"{FRONTEND_URL}/liff/practice"
            flex = FlexSendMessage(
                alt_text="建立練習表單",
                contents={
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {"type": "text", "text": "📝 請填寫練習資訊", "weight": "bold", "size": "md"},
                            {"type": "button", "action": {"type": "uri", "label": "前往填寫", "uri": liff_url}, "style": "primary"}
                        ]
                    }
                }
            )
            line_bot_api.reply_message(event.reply_token, flex)
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="❌ 只有管理員可以發起練習。"))
