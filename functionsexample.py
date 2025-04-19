"""
def painter():
    print("Painting")

painter()"""
###################3
#01) Create function called add(),sub(),mul(),div()
# And get the input  for a and b inside  every Functions then print the result.


def painter():
    print("Painting")

painter()

def add():
    a=int(input("enter num01:"))
    b=int(input("enter num02:"))
    print("Total=",a+b)

add()

def sub():
    a=int(input("enter num01:"))
    b=int(input("enter num02:"))
    print("Total=",a-b)

sub()

def div():
    a=int(input("enter num01:"))
    b=int(input("enter num02:"))
    print("Total=",a%b)
div()

def mul():
    a=int(input("enter num01:"))
    b=int(input("enter num02:"))
    print("Total=",a*b)
mul()


#########################

#02) Get a integer number from user and pass it to  the function called findpassorfail().
#let the function print ehether the user is pass or fail.

def findpassorfail():
    a=int(input("enter the mark ="))
    if (a >= 35 and a <=100):
        print("pass")
    else:
        print("fail")

findpassorfail()

##################################
#03) Get a integer number from user and pass it to the function called findevenorodd().
#let the function print ehether the number is even or odd.

def findevenorodd():
    a=int(input("enter the no:"))
    if (a%2==0):
        print("Even")
    else:
        print("Odd")

findevenorodd()

================

def oddoreven(b):
    if (b%2==0):
        print("Even")
    else:
        print("Odd")
a=int(input("enter the no:"))
oddoreven(a)


####################################
#04) Get input for a and b  and pass it to the function called printrange() let
#the function print numbers from  a to b.


def printrange():
    a=int(input("enter the a="))
    b=int(input("enter the b="))
    for i in range(a,b):
        #print(i,end="")
        print(i)

printrange()
======

def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)

printrange(1,22)

=====================


def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)

a=int(input("enter the a="))
b=int(input("enter the b="))
printrange(a,b)


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

====================
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

