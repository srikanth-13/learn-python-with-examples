"""
polymorphism

Polymorphism is a core concept in object-oriented programming (OOP).
It means "many forms" — the ability of a function, object, or method to take on different behaviors based on context.
"""
def add(a,b,c=0):
    print(a+b+c)
add(1,2)
add(1,2,3)
=================================
class animal():
    def sound(self):
        print("Animal Makes a Sound")


class dog(animal): #inherit
    pass


d1=dog()

d1.sound()


#1)  Create a class called   Animal With a method sound() that prints
# "Animal makes a sound." Create a derived class called Dog that inherits from
# Animal and overrides the sound() method to print "Dog  barks".
#Create another derived class called bird that inherits from Animal and overrides the
#sound() method to print "Birds sing"

class animal():
    def sound(self):
        print("Animal Makes a Sound")


class dog(animal):
    def sound(self):          #method overriding
        print("dog  barks")

class bird(animal):
    def sound(self):          #method overriding
        print("Bird  Sing")

d1=dog()

d1.sound()

b1=bird()
b1.sound()

a=animal()
a.sound()
