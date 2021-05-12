import requests
import json

# send a column of data to google sheet
def sendDataToGoogleSheet(url, payload):
    resp = requests.post(url, params=payload)

# return a dict of sheet
def getDataFromGoogleSheet(url, payload):
    if payload == 0:
        resp = requests.get(url, 0)
    else :
        resp = requests.get(url, payload)

    return json.loads(resp.text)
