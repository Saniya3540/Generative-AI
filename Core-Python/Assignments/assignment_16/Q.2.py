#2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
#e. Constructor (Support both parameterized and parameterless)
#f. Destructor
#g. ShowProduct
#h. Add static member discount.
#i. Provide methods for applying discount on price of product.

class Product:
    discount=5
    def __init__(self,pid=0,pname="",price=0,quantity=0):
        if pid==0 and pname=="" and price==0 and quantity==0:
            self.pid=int(input("Enter Product ID:"))
            self.pname=input("Enter Product name:")
            self.price=int(input("Enter Price:"))
            self.quantity=int(input("Quantity is:"))
            print("---------------------")
        else:
            self.pid=pid
            self.pname=pname
            self.price=price
            self.quantity=quantity

    def applyDiscount(self):
        x= self.price-(self.price*(Product.discount/100))
        return x


    def showProduct(self):
        print("Product ID:",self.pid)
        print("Product name:",self.pname)
        print("Price:",self.price)
        print("Quantity:",self.quantity)
        print("After Discount Price :",self.applyDiscount())
        print("-----------------------------")

    def __del__(self):
        print("Object is Destroyed")

p1=Product()
p1.showProduct()

p2=Product(101,"Book",1000,4)
p2.showProduct()

p3=Product(102,"Laptop",60000,3)
p3.showProduct()

