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
wait4input = False
orderCalled = time.time()

restaurantName = []
restaurantAddr = []

orderRequest = []
sum = 0

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

def loadShop(url):
    Data = getDataFromGoogleSheet(url)
    for outer in Data:
        for inner in Data.get(outer):
            if inner == 'NAME':
                restaurantName.append(Data.get(outer).get(inner))
            if inner == 'ADDRESS':
                restaurantAddr.append(Data.get(outer).get(inner))

loadGAS(jdata['Gas']['Get'][0]['baseExcel'])
loadShop(jdata['Gas']['Get'][1]['baseExcel'])

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
    global sum, orderRequest, ordering, orderCalled, wait4input
    message = ''
    msg = event.message.text 

    if wait4input == True:
        if 'c' == msg:
            ordering = False
            wait4input = False
            quitMessage = '結束點單,總價為:  ' + sum + ' 元'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=quitMessage))
            sum = 0
        else:
            splStr = msg.split(';')
            if len(splStr) == 3:
                items = splStr[0] + splStr[2]
                orderRequest.append(item)
                sum = sum + int(splStr[1])*int(splStr[2])
        return
    
    if ordering == True:
        if time.time()-orderCalled > 600 :
            ordering = False
            wait4input = False
        elif msg in restaurantName :
            getOrder(line_bot_api, event.reply_token, msg)
            wait4input = True
            return

    if 'RELOAD' == msg:
        loadGAS(jdata['Gas']['Get'][0]['baseExcel'])
        loadSheet(jdata['Gas']['Get'][1]['baseExcel'])
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
    if message != '' :
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
