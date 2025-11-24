#Q.8. Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!
n=int(input("Enter n:"))
sum=0
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    sum+=fact
print("sum of factorial series is:",sum)


#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
N=int(input("Enter N:"))
sum=0
for i in range(1,N+1):
    sum=sum+N**i
print("Sum is:",sum)


#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n=int(input("Enter n:"))
sum=0
x=1
for i in range(n):
    sum=sum+x
    x=x*2
print("Sum of Geometric Series is:",sum)


#d. S = a + (a^2) / 2 + (a^3)/ 3 + ...... + (a^10) / 10
a=int(input("Enter a:"))
sum=0
for i in range(1,11):
    sum=sum+(a**i)/i
print("Sum is:",sum)


#e. x – (x^2)/3 + (x^3)/5 – (x^4)/7 + .... to n terms
