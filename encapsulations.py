"""
Encapsulation means bundling data (variables)
and methods (functions) that operate on that data into a single unit (class),
and restricting direct access to some of the object's components.
"""


#private variable

class company():
    def __init__(self):
    #we can't override the private variables. 
        self.__companyname="Tata" #private variable __ we can use or access only inside the class functions
    def companyname(self):
        print(self.__companyname)
        
c=company()
c.companyname()



#protected variable
class company():
    def __init__(self):
    
        self._companyname="Tata" #public and protected private access modifiers , we can access variable derived class as well.

class b(company):
    pass
 
        
c=b()

print(c._companyname)




