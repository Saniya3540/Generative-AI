#1. Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook

class Book:
    def __init__(self,bid=0,bname="",price=0,author=""):
        if bid==0 and bname=="" and price==0 and author=="":
            self.bid=int(input("Enter Book id:"))
            self.bname=input("Enter book name:")
            self.price=int(input("Enter price:"))
            self.author=input("Enter author:")
            print("------------------------")
        else:
            self.bid=bid
            self.bname=bname
            self.price=price
            self.author=author

    def showBook(self):
        print("Book ID is:",self.bid)
        print("Name of the book is:",self.bname)
        print("Price of book is:",self.price)
        print("Book Author is:",self.author)
        print("========================")

    def __del__(self):
        print("Book is destroyed")

b1=Book()
b1.showBook()

b2=Book(101,"Atomic Habits",500,"James Clear")
b2.showBook()

