# pip install line-bot-sdk
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage, LocationSendMessage
)

line_bot_api = LineBotApi('bvHQUsARF8FHgreZkiBLDdRNlna+MnKFjDgqwJN3SIN5/bOUqStNGTm4xtm+FgxV172TFJVpPOx9pLNA4tNXc2PMm/1QLxgLGff7tYrqPM616Y2rRoFDLAbgI83pq63WXRhHwCxZbuGMZmIX+3IhjgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('37fb7a10e001dab27a359d07932554fc')