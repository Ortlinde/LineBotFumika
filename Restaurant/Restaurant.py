from ..Util.excelFunction import *

class Restaurant:
    sum = 0
    ordered = []

    def __init__(self,userId,jdata):
        self.jdata = jdata
        self.userId = userId
        
    def getId(self):
        return self.userId

    def addOrder(self, order):
        self.ordered.append(order)

    def push(self):
        pass

class EightWay(Restaurant):
    def push(self):
        payload = {
            'USER': self.userId,
            'PRICE': sum,
            'ITEMS': self.ordered }
        sendDataToGoogleSheet(self.jdata['Gas']['Get'][2]['baseExcel'], payload)

class YiTing(Restaurant):
    pass

class GuJing(Restaurant):
    pass