f=open("fruits")
content=f.read()
print(content)

f.write("jam")


============
f=open("fruits", "w")
f.write("jam\n") 
f.write("mango")
f.close()

f=open("fruits","r+")

print(f.read())

================

f=open("fruits", "a")
f.write("\napple\n") 
f.write("banana")
f.close()

f=open("fruits","r+")

print(f.read())
