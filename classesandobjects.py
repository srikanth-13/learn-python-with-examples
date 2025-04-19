class goa:
    name="srikant"
    drink=""
    def party(self):
        print("Lets party..........")
    def beach(self):
        print("swim in the beach.......")

ramesh = goa()
suresh = goa()

ramesh.name="ramesh"
suresh.name="suresh"
ramesh.drink="Yes"
suresh.drink="No"
print(ramesh.name)
print("Drink",ramesh.drink)
print(suresh.name)
print("Drink",suresh.drink)

ramesh.party()
suresh.beach()
#################
#1)  create class called laptop and create a following variables and functions.
#Variables=> Price,Processor,Ram
#create Object HP,DELL,Lenovo
class laptop:
    price=0
    proc=""
    Ram=""
hp=laptop()
dell=laptop()
hp.price=40000
hp.Ram="8Gb RAM"
hp.proc="i10"

dell.price=40000
dell.Ram="8Gb RAM"
dell.proc="i10"

print(hp.Ram)
print("dell laptop price is:", dell.price)

##########################
#2) create a class called kodaikanal and create as much variables you can and functions.


class kodaikanal():
    
    price=0
    def resort(self):
        print("Best resort in kodaikanal")
    def hut(self):
        print("affordable room")
    def lodge(self):
        print("luxuary rooms")

sri=kodaikanal()
family=kodaikanal()
bachelor=kodaikanal()

sri.price=400
family.price=600
bachelor.price=200
sri.lodge()
print("lodge price:", sri.price)
family.resort()
print("resort price:", family.price)
bachelor.hut()
print("hut price:", bachelor.price)
