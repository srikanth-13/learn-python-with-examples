"""
INSTANCE VARIABLES:
"""
class phone():
    
    def __init__(self,brand,price,charger):
        self.brand=brand
        self.price=price
        self.charger=charger
    def display(self):
        print("Brand:", self.brand)
        print("price:", self.price)
        print("charger:", self.charger)

samsung=phone("nokia","10000","C-Type")#(instance variable)

samsung.display()

print(" ")
redmi=phone("redmi","10000","C-Type") #(instance variable)
redmi.display()

===================================
"""
CLASS VARIABLES
"""

class phone():
    charger="C-TYPE" #class variable (for constant value for all objects)
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:", self.brand)
        print("price:", self.price)
        print("charger:", self.charger)

samsung=phone("nokia","10000")#(instance variable)(for mutable values)

samsung.display()

print(" ")
redmi=phone("redmi","20000") #(instance variable)
redmi.display()

+++++++
class phone():
    charger="C-TYPE" #class variable
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:", self.brand)
        print("price:", self.price)
        print("charger:", self.charger)

phone.charger="B-Type"
samsung=phone("nokia","10000")#(instance variable)

samsung.display()

print(" ")
redmi=phone("redmi","20000") #(instance variable)
redmi.display()

============================================

"""

"""
