"""
Inheritence
"""

class dad():
    def phone(self):
        print("Dads Phone")
class son(dad): #single inheritance
    def laptop(self):
        print("son's laptop")


ram=son()
ram.phone()


================
#single object  can acces multiple class variables. 
class dad():
    def phone(self):
        print("Dads Phone")

class mom():
    def sweet(self):
        print("moms sweet")
class son(dad,mom):   #multiple inheritance
    def laptop(self):
        print("son's laptop")


ram=son()
ram.phone()
ram.sweet()

++++++++++

class grandpa():
    def phone(self):
        print("Dads Phone")

class dad(grandpa):
    def money(self):
        print("dad money")
class son(dad):   #multiple inheritance
    def laptop(self):
        print("son's laptop")


ram=son()
ram.phone()

#multi level  inheritance
============================
#Hierarchical Inheritance

'''Multiple child classes inherit from a single parent class.'''

class dad():
    def money(self):
        print("grandpa money")
class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass


s2=son2()
s2.money()
=============================
#Hybrid Inheritance

'''Combination of multiple types of inheritance.'''
class dad():
    def money(self):
        print("grandpa money")

class land():
    def ola(self):
        print("important land")
class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass


s2=son2()
s2.money()

s1=son1()
s1.ola()


