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

    def push(self,shopExcel):
        payload = {
            'USER': self.userId,
            'PRICE': sum,
            'ITEMS': self.ordered }
        sendDataToGoogleSheet(self.jdata['Gas']['Get'][2][shopExcel], payload)

class EightWay(Restaurant):
    def push(self):
        super().push("eightWayExcel")

class YiTing(Restaurant):
    def push(self):
        super().push("yiTingExcel")

class GuJing(Restaurant):
    def push(self):
        super().push("guJingExcel")