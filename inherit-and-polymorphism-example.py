"""
01) Create a base class called Shape with a method area() that returns 0.
Create a derived class called Rectangle that inherits from Shape and
overrides the area() method to calculate and return the area of a rectangle.
"""

#solution:

class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        return 1

r=rectangle()

print(r.area())
##########
class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)
r=rectangle()

r.area()

=======================
"""
02)Create a base class called Person with a constructor that takes a name as a parameter.
Create a derived class called Student that inherits from Person and
has a constructor that takes a parameter called grade.
Write a method in Student to display the name and grade of the  student.
Use Super Keyword to achieve this.
"""
#solution:

class person():
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,grade):
        super().__init__(name) #using super keyword we can call base class functions.
        self.grade=grade
    def display(self):
        print(self.grade)
        print(self.name)
    
    


s=student("john","A")



s.display()



================================================
"""
03) Create a base class called Vehicle with a method start() that prints "Vehicle started."
Create a derived class called Car that inherits from Vehicle and 
overrides the start() method to print "Car started."
"""
#solution
class Vehicle:
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def start(self):
        print("Car started.")

# Example usage
c = Car()
c.start()


====================================


"""
04) Create a base class called Employee with properties name and salary.
Create a derived class called Manager that inherits from Employee and
adds a property department.
Write a method in Manager to display the name, salary, and
department of the manager.
"""

#solution:
#Manual Attribute Assignment info funtions never used.

class employee():
    def info(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def details(self,name,salary,department):
        self.department=department

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print     ("Department:",self.department)


m=manager()

m.name="srikanth"
m.salary="45000"
m.department="Devops"

m.display()
++++++++++++++++++++++++++++++++++
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

# Example usage
m = Manager("Srikanth", 45000, "DevOps")
m.display()
