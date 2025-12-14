#3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
#j. Constructor (Support both parameterized and parameterless)
#k. Destructor
#l. ShowShirt
#m. For each size of shirt price should change by 10%.
#(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept.
class Shirt:
    size_increment={"small":0, "medium":10, "large":20,"xlarge":30 }
    def __init__(self,sid=0,sname="",type="",price=0,size=""):
        if sid==0 and sname=="" and type=="" and price==0 and size=="":
            self.sid=int(input("Enter Shirt ID:"))
            self.sname=input("Enter Product Name:")
            self.type=input("Shirt Type:")
            self.price=int(input("Enter Price:"))
            self.size=input("Size of Shirt:")
            print("------------------------------")
        else:
            self.sid=sid
            self.sname=sname
            self.type=type
            self.price=price
            self.size=size
 

    def changePrice(self):
        size1 = self.size.lower() 
        if size1 in Shirt.size_increment:
            percent = Shirt.size_increment[size1]
            new_price = self.price + (self.price * percent / 100)
            return new_price
        else:
            return self.price 
            
    def showShirt(self):
        print("Shirt ID:",self.sid)
        print("Shirt Name:",self.sname)
        print("Shirt Type:",self.type)
        print("Price:",self.price)
        print("Size:",self.size)
        print("Change Price:",self.changePrice())
        print("------------------------------")

    def __del__(self):
        print("Destroyed!")
        print("------------------------------")

s1=Shirt()
s1.showShirt()

s2=Shirt(111,"AAA","Formal",1000,"Small")
s2.showShirt()

s3=Shirt(222,"BBB","No Formal",500,"Large")
s3.showShirt()

s4=Shirt(333,"CCC","Formal",1200,"Medium")
s4.showShirt()