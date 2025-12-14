#Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
#d. Add static variable count and also maintain count of objects created.
class Book:
    count=0
    def __init__(self,bid=0,bname="",price=0,author=""):
        if bid==0 and bname=="" and price==0 and author=="":
            self.bid=int(input("Enter Book ID:"))
            self.bname=input("Book name is:")
            self.price=int(input("Enetr price:"))
            self.author=input("Author is:")
            print("------------------------------")

        else:
            self.bid=bid
            self.bname=bname
            self.price=price
            self.author=author
        Book.count+=1    
 

    def showBook(self):
        print("Book id is:",self.bid)
        print("Book name is:",self.bname)
        print("Price is:",self.price)
        print("Author is:",self.author)
        print("-------------------------------")

    def __del__(self):
        print("Book is Destroyed!")
        print("----------------------------------------")

b1=Book()
b1.showBook()

b2=Book(101,"AAA",1000,"aa")
b2.showBook()

b3=Book(102,"BBB",500,"bb")
b3.showBook()

b4=Book(103,"CCC",800,"cc")
b4.showBook()

print("Total no. of objects created:",Book.count)