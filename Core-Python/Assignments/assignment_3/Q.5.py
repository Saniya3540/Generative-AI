#Q.5. WAP to check whether the triangle is equilateral, isosceles or scalene triangle.
A=float(input("Enter 1st side:"))
B=float(input("Enter 2nd side:"))
C=float(input("Enter 3rd side:"))
if A==B==C:
    print("Triangle is Equilateral!")
elif A==B or B==C or C==A:
    print("Triangle is Isosceles")
else: 
    print("Triangle is Scalene")
