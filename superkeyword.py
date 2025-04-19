'''
super keyword:
The super() keyword in Python is used to call methods from a parent class.
It's most commonly used inside a child class to call the constructor (__init__) or other methods of the parent class.
'''

class a():
    def __init__(self):
        print("A")
    def display(self):
        print("You are in class a")
class b():
    def __init__(self):
        super().__init__()
        print("B")

    def display(self):
        print("you are in class b")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("c")

    def display(self):
        print("you are in class c")


ob2=c()

ob2.display()
