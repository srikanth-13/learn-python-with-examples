################for-loop-exercise#####
#01) Get input for number a and b

a=5
b=10

for i in range(a,b)
    print(i)

========
a=int(input())
b=int(input())

for i in range(a+1,b):
    print(i)

#######################################################
    
#02)  print even number between 1 to 10.


for i in range(1,11):
    if (i%2==0):
         print(i)
         
###################################################3

#03) count the number of odd numbers between 1 to 10.
         
count=0
for i in range(1,11):
    if (i%2==1):
         count=count+1
print(count)      

###################################################

#04)  count the  number  of odd and even  numbers between 1 to 10 and print it.
odd=0
even=0
for i in range(1,11):
    if (i%2==1):
         odd=odd+1
    else:
        even=even+1
print("Even no count:",even)
print("Odd no count:",odd)
#######################################################

#05) count the  number which are divisible by 3 and 5

#Range 1-100

count=0
for i in range(1,100):
    if (i%3==0 and i%5==0):
        count=count+1
print(count)

#########################################
#06)Write s program to compute the sum of the first 5 natural numbers
sum=0

for i in range(1,6):
    sum=i+1
print(sum)

#######################################

#07) Write a program to read 10 numbers from the  keyboard and find their sum and average.
a=[]
for i in range(10):
    num=int(input())
    a.append(num)
print(a)
============================
a=[]
print("Enter 10 Numbers:")
for i in range(10):
    num=int(input("Enter num "+ str(i)+":"))
    a.append(num)
print(a)
===================================
a=[]
print("Enter 10 Numbers:")
for i in range(10):
    num=int(input("Enter num "+ str(i+1)+":"))
    a.append(num)
print(a)

########################################

#08) Write a program to display  n terms of natural and their sum Test Data: 7

a=[]
print("Enter the 7 natural numer:")
for i in range(8):
    num=int(input("enter the num "+ str(i+1)+":"))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)

########################################
#09) write a Program to display  the cube  of the  number up to integer. Test data :5
for i in range(1,6):
    print(i**3)


########################################

#10) Write a program to display  a pattern  like a right angle  triangle using an asterisk.
#nested loop
for i in range (1,5):
    print()
    for j in range(1,i+1):
        print("*" , end=" ")


 
