from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from Restaurant.Restaurant import Restaurant
import time

# 點餐
def order():
    message = TemplateSendMessage(
        alt_text='今天想吃什麼呢？',
        template=ButtonsTemplate(
            thumbnail_image_url="https://www.kamigo.tw/assets/kamigo-c3b10dff4cdb60fa447496b22edad6c32fffde96de20262efba690892e4461e8.png",
            title="今天想吃什麼呢？",
            text="10分鐘內未點單請重新呼叫",
            actions=[
                MessageTemplateAction(
                    label="今天想吃古今中外",
                    text="古今中外"
                ),
                MessageTemplateAction(
                    label="或是來點八方雲集",
                    text="八方雲集"
                ),
                MessageTemplateAction(
                    label="還是想要宜廷小吃",
                    text="宜廷小吃"
                ),
                MessageTemplateAction(
                    label='下一頁',
                    text='下一頁'
                )
            ]
        )
    )
    return message

def getOrder(api, token, msg):
    api.reply_message(token, TextSendMessage(text=isinstance(msg, Restaurant)))