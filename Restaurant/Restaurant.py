class Restaurant:
    def __init__(self,name):
        self.name = name
        
    def getName(self):
        return self.name

    def toString(self):
        return str(type(self))