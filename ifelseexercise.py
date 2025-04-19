#1)Get input for variables mark. if mark > 35 print pass. Else print fail

mark=int(input("Enter your mark:" ))
if (mark >= 35):
    print("pass")
else:
    print("fail")

################################################################################


#2) Get input for variables income. if incomes is greater than 7000 scholarship is available. Else not eligible for scholarship

income=int(input("Enter your income:" ))

if (income > 7000):
    print("Your eligible for scholarship")
else:
    print("Your not eligible for scholarship")
##############################################################################

#3) Get input for number and check  whether it is divisible by both 3 and 5 or not. if yes then print, the number is divisible by 3 and 5 else print the number is not divisble by 3 and 5.

#basic
num=int(input("Enter the No:" ))

if (num%3==0):
    print("Divisible by 3")
else:
    print("Not Divisible by 3")
#solution

num=int(input("Enter the Num:" ))
if(num%3==0 and num%5==0):
    print("Divisible by 3 and 5")
else:
    print("Not Divisible by 3  and 5")

###############################################################################
#4) Get input for a number  and find it is  even or odd.

num=int(input("Get a num4:"))

if(num%2==0):
    print("It is an Even Number")
else:
    print("It is an ODD Number")
    
######################################################################################

#5) get input for score out of 100.
   #if score is < 35 = "Poor student"
   #if score is greater than  35 but < than 70 , print "Average student"
   # if score is greater than 70, print "Good student"

#normal method
score=int(input("Enter the score:" ))

if(score < 35):
    print("Poor student")
if (score > 35 and score < 70):
    print("Average student")
if (score > 70 ):
    print("Good student")

#better way is use "elif" (for reduce execution time).

print("5) get input for score out of 100.")
score=int(input("Enter the score:" ))
if(score < 35):
    print("Poor student")
elif (score > 35 and score < 70):
    print("Average student")
else:
    print("Good student")
#alternative
print("5) get input for score out of 100. second sol:")

score=int(input("Enter the score:"))

if (score < 35):
    print("Poor student")
elif (score > 35 and score < 70):
    print("Average student")
elif (score > 70 and score < 100):
    print("Good student")
else:
    print("Invalid Input")


##########################################################

#6) Make mini calculator, Get input for 2 numbers A and B , Get input from user whether to add/sub/mul/div, if users selects add then add the two numbers and print the result.

#Solution:

print("Tasks 06:")
a=int(input("A:"))
b=int(input("B:"))
operation=input("add/sub/mul/div:")
if (operation=="add"):
    print(a+b)
elif (operation=="sub"):
    print(a-b)
elif (operation=="mul"):
    print(a*b)
elif (operation=="div"):
    print(a/b)
else:
    print("invalid operations")

######################################################################
#7). Get  a input for score percentage. only if the percentage is greater than 70, get input for his name, department and location. Then print you are eligible. if not print you are not eligible.
per=int(input("enter the student percentage:"))

if(per >= 70):
    name=input("Enter your name:")
    department=input("Enter your department:")
    location=input("Enter your location:")
    print("you are eligible")
else:
    print("not eligible")
##############################################################3
#8). Get  input for salary and age .
    #if salary greater than  or equal  to 20000 or  age less than or equal to 25, get  input for required loan amount.if not print you are not eligible for loan.
    #if required loan amount is less tha or equal to 50,000 print you are eligible  for loan. if it is greater than 50,000 print maximum loan amount is 50,000.
#nested if
sa=int(input("Enter your salary:"))
age=int(input("Enter your age:"))

if (sa >= 20000 or age <= 25):
    loan=int(input("Enter the loan amount:"))
    if (loan > 50000):
        print("Maximum loan amount is 50000")
    else:
        print("you are eligible for loan")
else:
    print("your not eligible for loan")


#9) get input for five subjects marks. add all of it and find average. if average mark is less than 35. Print "Additional claa is required" else Print "you are good to go"

a=int(input("sub01:"))
b=int(input("sub02:"))
c=int(input("sub03:"))
d=int(input("sub04:"))
e=int(input("sub05:"))

f=((a+b+c+d+e)/5)
if (f < 35 ):
    print("Additional claa is required")
else:
    print("you are good to go")

    
