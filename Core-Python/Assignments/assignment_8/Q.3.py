#Q.3. Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
def sum_of_series(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
n=int(input("Enter n:"))
print("Sum is:",sum_of_series(n))


#b. 1!+ 2! + 3! + 4!+..... + n!
def sum_of_fact(n):
    total=0
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        total+=fact
    return total
n=int(input("Enter n:"))
print("Sum of factorial is:",sum_of_fact(n))


#c. 1^1 + 2^2 + 3^3+ ...... n^n
def series(n):
    total=0
    for i in range(1,n+1):
        ans=i**i
        total+=ans
    return total
n=int(input("Enter n:"))
print("result is:",series(n))