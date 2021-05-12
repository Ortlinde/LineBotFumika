from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import time

# 點餐
def order():
    message = TemplateSendMessage(
        alt_text='今天想吃什麼呢？',
        template=ButtonsTemplate(
            thumbnail_image_url="https://www.kamigo.tw/assets/kamigo-c3b10dff4cdb60fa447496b22edad6c32fffde96de20262efba690892e4461e8.png",
            title="今天想吃什麼呢？",
            text="10分鐘內未點單請重新呼叫,點單時請按照\"品項 單價 數量\"的順序輸入,如要結帳請輸入\"c\"",
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
        '''message = TemplateSendMessage(
            alt_text='今天想吃什麼呢？',
            template=ButtonsTemplate(
                thumbnail_image_url="https://www.kamigo.tw/assets/kamigo-c3b10dff4cdb60fa447496b22edad6c32fffde96de20262efba690892e4461e8.png",
                title="今天想吃什麼呢？",
                text="任一單品+150元可升級套餐",
                actions=[
                    MessageTemplateAction(
                        label="精緻特選炒飯",
                        text="精緻特選炒飯"
                    ),
                    MessageTemplateAction(
                        label="主廚推薦",
                        text="主廚推薦"
                    ),
                    MessageTemplateAction(
                        label="湯品、沙拉、甜點",
                        text="湯品、沙拉、甜點"
                    ),
                    MessageTemplateAction(
                        label="飲料",
                        text="飲料"
                    ),
                    MessageTemplateAction(
                        label="下一頁",
                        text="下一頁"
                    )
                ]
            )
        )'''
        message = ImageSendMessage(
            original_content_url='https://cdn.walkerland.com.tw/images/upload/poi/p59576/m67980/41a28f0dbbebff13c66325c817ad0de25bee8690.jpg',
            preview_image_url='https://cdn.walkerland.com.tw/images/upload/poi/p59576/m67980/41a28f0dbbebff13c66325c817ad0de25bee8690.jpg'
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
    #api.reply_message(token, TextSendMessage(text='點單時請按照\"品項 單價 數量\"的順序輸入,如要結帳請輸入\"c\"'))