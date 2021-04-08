# just for test function
import json

with open('keyword.json', mode='r', encoding='utf8') as jfile:
    keyword = json.load(jfile)

for key in keyword:
    print(key)