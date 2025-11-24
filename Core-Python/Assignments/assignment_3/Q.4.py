#Q.4. WAP to input all sides of a triangle and check whether triangle is valid or not.
A=float(input("Enter 1st side:"))
B=float(input("Enter 2nd side:"))
C=float(input("Enter 3rd side:"))
if A+B>C and A+C>B and B+C>A:
   print("Triangle is Valid")
else:
   print("Triangle is not valid!")



