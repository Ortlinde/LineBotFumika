import requests
import time

# send a column of data to google sheet
def sendDataToGoogleSheet(url, payload):
    resp = requests.post(url, params=payload)

# return a dict of sheet
def getDataFromGoogleSheet():
    resp = requests.get(url, 0)

    return json.loads(resp.text)
