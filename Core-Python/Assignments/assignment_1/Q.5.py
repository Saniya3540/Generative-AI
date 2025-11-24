#5. Write a program to enter P,T,R and calculate compound interest:
P=float(input("Enter Principle amount:"))
T=float(input("Enter time :"))
R=float(input("Enter Rate of interest:"))
A=P*(1+(R/100))**T
CI= A- P
print("Compound Interest is:",CI)