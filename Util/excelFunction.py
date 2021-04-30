import requests
import json
import time

with open('./JSON/config.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

def sendDataToGoogleSheet(name, value):
    url = jdata['Gas']['Get'][0]['baseExcel']
    payload = {
        'DATE': time.strftime("%Y-%m-%d", time.localtime()),
        'NAME': name,
        'VALUE': value }
    resp = requests.post(url, params=payload)
    print(resp.text)

# return a dict of sheet
def getDataFromGoogleSheet():
    url = jdata['Gas']['Get'][0]['baseExcel']
    resp = requests.get(url, 0)

    return json.loads(resp.text)
