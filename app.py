### main function ###

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import json

#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from order import *
from .Util.excelFunction import *
#==============================

#========python library========
import tempfile, os
import datetime
import time
#==============================

# load json setting file
with open('./JSON/config.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
with open('./JSON/keyword.json', mode='r', encoding='utf8') as jfile:
    keyword = json.load(jfile)

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(jdata['TOKEN'])
# Channel Secret
handler = WebhookHandler(jdata['Webhook'])

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# handle message
@handler.add(MessageEvent, message = TextMessage)
def handle_message(event):
    msg = event.message.text
    #message = TextSendMessage(text='you say: \n' + event.message.text)
    #line_bot_api.reply_message(event.reply_token, message) # 回復

    keyList = []
    valueList = []
    reactDict = {}

    message = ''
    #for key in keyword:
    #    keyList.append(key)
    kvData = getDataFromGoogleSheet()
    for outer in kvData:
        for inner in kvData.get(outer):
            if inner == 'NAME':
                keyList.append(kvData.get(outer).get(inner))
            if inner == 'VALUE':
                valueList.append(kvData.get(outer).get(inner))
    
    for i in range(len(keyList)):
        reactDict[keyList[i]] = valueList[i]

    if msg in keyList:
    #    message = TextSendMessage(text=keyword[msg])
        message = TextSendMessage(text=reactDict.get(msg))
    elif '點餐' in msg:
        message = order_panel()
    line_bot_api.reply_message(event.reply_token, message)
    '''if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)'''

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
