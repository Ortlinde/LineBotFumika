from Util.excelFunction import *

class Restaurant:
    sum = 0
    ordered = ""

    def __init__(self,userId,jdata):
        self.jdata = jdata
        self.userId = userId
        
    def getId(self):
        return self.userId

    def addOrder(self, order):
        if self.ordered == "":
            self.order = order
        else:
            self.ordered = self.order + "," + order

    def push(self,shop):
        payload = {
            'USER': self.userId,
            'PRICE': sum,
            'ITEMS': self.ordered,
            'SHOP' : shop }
        sendDataToGoogleSheet(self.jdata['Gas']['Get'][2]['shopExcel'], payload)

class EightWay(Restaurant):
    def push(self):
        super().push(0)

class YiTing(Restaurant):
    def push(self):
        super().push(1)

class GuJing(Restaurant):
    def push(self):
        super().push(2)