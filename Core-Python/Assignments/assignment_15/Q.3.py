#3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
#g. Constructor (Support both parameterized and parameterless)
#h. Destructor
#i. ShowShirt

class Shirt:
    def __init__(self,sid=0,sname="",type="",price=0,size=""):
        if sid==0 and sname=="" and type=="" and price==0 and size=="":
            self.sid=int(input("Enter Shirt ID:"))
            self.sname=input("Shirt Name is:")
            self.type=input("Shirt type:")
            self.price=int(input("ENetr Shirt Price:"))
            self.size=input("Size of Shirt:")
            print("-------------------------")
        else:
            self.sid=sid
            self.sname=sname
            self.type=type
            self.price=price
            self.size=size

    def showShirt(self):
        print("Shirt ID is:",self.sid)
        print("Shirt Name is:",self.sname)
        print("Shirt type:",self.type)
        print("Price of shirt:",self.price)
        print("Size is:",self.size)
        print("-------------------------------")

    def __del__(self):
        print("Shirt is Destroyed!")
        print("-------------------------------")

s1=Shirt()
s1.showShirt()

s2=Shirt(102,"XYZ","Formal",1000,"Small")
s2.showShirt()