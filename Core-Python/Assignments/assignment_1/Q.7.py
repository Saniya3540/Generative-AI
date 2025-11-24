#7. Program to find the roots of a Quadratic Equation
a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))
dis=(b**2)-(4*a*c)
x1 = (-b + (dis**0.5)) / (2*a)
x2 = (-b - (dis**0.5)) / (2*a)
print("Roots are:", x1, "and", x2)