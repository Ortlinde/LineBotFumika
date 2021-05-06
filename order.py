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

def getOrder(msg):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=type(msg)))

def order_panel():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='上一頁',
                            data='next_page_0'
                        ),
                        PostbackTemplateAction(
                            label='下一頁',
                            data='next_page_1'
                        ),
                        PostbackTemplateAction(
                            label='結束',
                            data='end'
                        )
                    ]
                )
            ]
        )
    )
    return message