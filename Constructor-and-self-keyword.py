"""
What is constructor:

A Constructor is a unique function that gets  called  automatically when an object is created of a class
"""


class laptop():
    def __init__(self):
        self.price=0
        self.ram=""
    def display(self):
        print("price",self.price)
        print("ram",self.ram)


hp=laptop()
hp.price=3000
hp.ram="8GB"
dell=laptop()
dell.ram="16gb"
dell.price=5000
print(hp.display())
print(dell.display())
###############################

#1) Create a class called student.
#create a variable = name and register number using constructor.
#Create a funtion called disply which should display the name and register number
#of the student.


class student():
    def __init__(self):
        self.name=""
        self.reg_no=0
    def display(self):
        print("Name:",self.name)
        print("Reg_no:",self.reg_no)

info=student()

info.name="srikanth"
info.reg_no=32
print(info.display())

===========================================
class teacher():
    def __init__(self):
        self.name="srikanth"
        self.reg="123324"
    def display(self):
        print("Name:", self.name)
        print("Reg no:", self.reg)


s=teacher()

print(s.name)
print(s.reg)
s.display()
===================================================

class teacher():
    def __init__(self):
        self.name="srikanth"
        self.reg="123324"
    def display(self):
        print("Name:", self.name)
        print("Reg no:", self.reg)


s1=teacher()
s2=teacher()

s1.name="sri"
s1.reg="653"

s2.name="don"
s2.reg="243"


s1.display()
s2.display()



#############################

#2) Create a class called Fruit
#Create a variable called  color using __init__ method
#Create a object called apple "Pass the color variable as a parameter
#Thorugh object".

class fruit():
    def __init__(self):
        self.color=""

apple=fruit()

apple.color="red"
print(apple.color)

==================
class fruit():
    def __init__(self):
        self.color=""
    def display(self):
        print("color=", self.color)

apple=fruit()

apple.color="red"


apple.display()
============================

class fruit():
    def __init__(self,col):
        self.color=col

apple=fruit("red")
print(apple.color)




################################

#3) Create a class called teacher
#Create a variable = name and register number using constructor
#Create a function called display which should display the name and register number
#of the teacher

class teacher():
    def __init__(self, name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print("Name:", self.name)
        print("Reg no:", self.reg)


s=teacher("srikanth",544)
t=teacher("shri",543)

s.display()
t.display()
==========================
#######################################

"""
4) Create a class called calculator
Create 2 variables a and b. create a function called add,sub,mul,div
all funtions should take 2 variables as parameter.
pass a and b value through object().
"""
class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("ADD:", self.a+self.b)
        print("sub:", self.a-self.b)
        print("mul:", self.a*self.b)
        print("div:", self.a/self.b)


cal=calculator(10,20)

cal.display()
