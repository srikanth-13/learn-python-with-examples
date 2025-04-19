
def validate():
    return "i am devops engineer"
print(validate())


########################################
#05) Set s_username="EMC" s_password="123" ,Get input from username password, create
#function called validate. if uname and password matches the function should return true else false.

u_n="sri"
pass_word="123"

name=input("enter the name:")
passw=input("enter the passwd:")

def validate():
    if(u_n==name and pass_word==passw):
        print("correct")
    else:
        print("wrong")

validate()
===============
u_n="sri"
pass_word="123"

name=input("enter the name:")
passw=input("enter the passwd:")

def validate():
    if(u_n==name and pass_word==passw):
        return True
    else:
        return  False

a=validate()
print(a)




############################################
#06)(a+b)*c
#Get input  for a and b for  function called add ()  which should retorn the sum of a and b
# and multiply that sum with c.


def add(n1,n2):
    return n1+n2

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

added=add(a,b)
output=added*c

print(output)

