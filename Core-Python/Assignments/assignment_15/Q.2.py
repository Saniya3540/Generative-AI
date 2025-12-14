#2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
#d. Constructor (Support both parameterized and parameterless)
#e. Destructor
#f. ShowProduct

class Product:
    def __init__(self,pid=0,pname="",price=0,quantity=0):
        if pid==0 and pname=="" and price==0 and quantity==0:
           self.pid=int(input("Enter Product ID:"))
           self.pname=input("Enter Product name:")
           self.price=int(input("Price of Product:"))
           self.quantity=int(input("Quantity is:"))
           print("------------------------------")
        else:
            self.pid=pid
            self.pname=pname
            self.price=price
            self.quantity=quantity

    def showProduct(self):
        print("Product ID:",self.pid)
        print("Prodcut Name:",self.pname)
        print("Price:",self.price)
        print("Quantity is:",self.quantity)
        print("----------------------------------")

    def __del__(self):
        print("Product is Destroyed")
        print("---------------------------")

p1=Product()
p1.showProduct()

p2=Product(101,"Laptop",60000,2)
p2.showProduct()
        
