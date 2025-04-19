"""
method is nothing but functions.
"""

class laptop():
    charger="C-TYPE" 
    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self,price):
        self.price=price
    def getprice(self):   #instance method
        print(self.price)
    @classmethod     
    def setcharger(cls):
        cls.charger="B-Type"
        print("change the charger type B")
    @staticmethod
    def info():
        print("this my static method")

hp=laptop()
hp.brand="HP"
hp.setprice(2000)
hp.getprice()
print(hp.brand)

laptop.setcharger()
hp.info()



#when we assign value to objects using self keyword parameter that is called instance method.

#class method

#static method
