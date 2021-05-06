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
from Util.excelFunction import *
import Restaurant.Restaurant
#==============================

#========python library========
import tempfile, os
import datetime
import time
#==============================

# load json setting file
with open('./JSON/config.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(jdata['TOKEN'])
# Channel Secret
handler = WebhookHandler(jdata['Webhook'])

# 全域變數
reactDict = {}

ordering = False
orderCalled = time.time()

restaurantName = []

message = ''

# reload google sheet
def loadGAS(url):
    keyList = []
    valueList = []
    kvData = getDataFromGoogleSheet(url)
    
    for outer in kvData:
        for inner in kvData.get(outer):
            if inner == 'NAME':
                keyList.append(kvData.get(outer).get(inner))
            if inner == 'VALUE':
                valueList.append(kvData.get(outer).get(inner))
    
    for i in range(len(keyList)):
        reactDict[keyList[i]] = valueList[i]

def loadSheet(url, *list):
    Data = getDataFromGoogleSheet(url)
    
    for outer in Data:
        for inner in Data.get(outer):
            i = 0
            if i > 1:
                for l in list:
                    l.append(Data.get(outer).get(inner))
            i = i + 1 

loadGAS(jdata['Gas']['Get'][0]['baseExcel'])
loadSheet(jdata['Gas']['Get'][1]['baseExcel'], restaurantName)

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
    global message, ordering, orderCalled
    msg = event.message.text 
    
    if ordering == True:
        if time.time()-orderCalled > 600 :
            ordering = False
        elif msg in restaurantName :
            #getOrder(Restaurant(msg))
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='1'))

    if 'RELOAD' == msg:
        loadGAS(jdata['Gas']['Get'][0]['baseExcel'])
        loadSheet(jdata['Gas']['Get'][1]['baseExcel'], restaurantName)
    elif '點餐' in msg:
        message = order()
        ordering = True
        orderCalled = time.time()
    elif msg in reactDict:
       message = TextSendMessage(text=reactDict.get(msg))
    elif 'setKey;' in msg:
        splitStr = msg.split(';')
        if len(splitStr) == 3:
            payload = {
                'DATE': time.strftime("%Y-%m-%d", time.localtime()),
                'NAME': splitStr[1],
                'VALUE': splitStr[2] }
            sendDataToGoogleSheet(jdata['Gas']['Get'][0]['baseExcel'], payload)
    # 回復訊息
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
