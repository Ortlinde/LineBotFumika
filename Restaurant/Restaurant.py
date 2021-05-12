from Util.excelFunction import *

class Restaurant:
    sum = 0
    ordered = ""

    def __init__(self,userId,jdata,shop):
        self.jdata = jdata
        self.userId = userId
        self.shop = shop
        
    def getId(self):
        return self.userId

    def addOrder(self, order):
        if self.ordered == "":
            self.order = order
        else:
            self.ordered = self.order + "," + order

    def push(self):
        payload = {
            'USER': self.userId,
            'PRICE': sum,
            'ITEMS': self.ordered,
            'SHOP' : self.shop }
        sendDataToGoogleSheet(self.jdata['Gas']['Get'][2]['shopExcel'], payload)