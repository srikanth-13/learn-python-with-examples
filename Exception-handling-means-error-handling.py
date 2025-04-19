"""
"""


#compile time error: during compiling its pop error
"""
code:

print("hi")
print("h")
printt("i")
==========
#output

Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/srikanth/python/roughnote.py", line 3, in <module>
    printt("i")
NameError: name 'printt' is not defined
"""

#logical error:
"""
a=10
b=20
print(a+a)
"""


#Runtime error

"""
a=int(input())
b=int(input())

print(a+b)
================
#output:
30
dsjh
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/srikanth/python/roughnote.py", line 3, in <module>
    b=int(input())
ValueError: invalid literal for int() with base 10: 'dsjh'
"""



#to solve above errors we are gonna use Exception handling:

try:
    a=int(input())
    b=int(input())
    print(a+b)
except Exception:
    print("somthing")


===========
try:
    a=int(input())
    b=int(input())
    c=input()
    print(c/a)

except ValueError as e:
    print("ValueError",e)
===========



try:
    a=int(input())
    b=int(input())
    c=input()
    print(d)

except ValueError as e:
    print("ValueError",e)

except TypeError as e:
    print("TypeError",e)

except Exception:
    print("something")

==========================    
#if everything works fine it will execute finally parameter:

try:
    a=int(input())
    b=int(input())
    c=input()


except ValueError as e:
    print("ValueError",e)

except TypeError as e:
    print("TypeError",e)

except Exception:
    print("something")

finally:
    print("done")
