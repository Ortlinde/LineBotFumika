from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from Restaurant.Restaurant import *
import time

# 點餐
def order():
    message = TemplateSendMessage(
        alt_text='今天想吃什麼呢？',
        template=ButtonsTemplate(
            thumbnail_image_url="https://www.kamigo.tw/assets/kamigo-c3b10dff4cdb60fa447496b22edad6c32fffde96de20262efba690892e4461e8.png",
            title="今天想吃什麼呢？",
            text="10分鐘內未點單請重新呼叫,點單時請按照\"品項;單價;數量\"的順序輸入,如要結帳請輸入\"c\"",
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
                )
            ]
        )
    )
    return message

def getOrder(api, token, msg):
    if msg == "古今中外":
        message = ImageSendMessage(
            original_content_url='https://example.com/original.jpg',
            preview_image_url='https://example.com/preview.jpg'
            )
        api.reply_message(token, message)
    elif msg == "八方雲集":
        message = ImageSendMessage(
            original_content_url='https://pic.pimg.tw/boda02/1557319378-1227573607_wn.jpg',
            preview_image_url='https://pic.pimg.tw/boda02/1557319378-1227573607_wn.jpg'
            )
        api.reply_message(token, message)
    else:
        message = ImageSendMessage(
            original_content_url='https://example.com/original.jpg',
            preview_image_url='https://example.com/preview.jpg'
            )
        api.reply_message(token, message)
    #api.reply_message(token, TextSendMessage(text='點單時請按照\"品項;單價;數量\"的順序輸入,如要結帳請輸入\"c\"'))