import requests
import json

with open('../JSON/config.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

def SendDataToGoogleSheet():
    url = jdata['Gas']['Get'][0]['baseExcel']
    payload = {'ID': 2,
               'DATE': 20210429,
               'NAME': 'A',
               'VALUE': 'B'
              }
    resp = requests.get(url, params=payload)
    print(resp.text)

# return a dict of sheet
def getDataFromGoogleSheet():
    url = jdata['Gas']['Get'][0]['baseExcel']
    resp = requests.get(url, 0)

    return json.loads(resp.text)

keyList = []
valueList = []
reactDict = {}

message = ''
kvData = getDataFromGoogleSheet()
for outer in kvData:
    for inner in kvData.get(outer):
        if inner == 'NAME':
            keyList.append(kvData.get(outer).get(inner))
        if inner == 'VALUE':
            valueList.append(kvData.get(outer).get(inner))
    
for i in range(len(keyList)):
    reactDict[keyList[i]] = valueList[i]

print(reactDict)
