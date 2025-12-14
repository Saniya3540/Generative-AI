#1. Write a program to find sum of following series using recursive functions:
#i. 1! + 2! + 3! + 4! +..... + n!
n=int(input("Enter n:"))
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
    
def sum_of_series(n):
    if n==1:
        return fact(1)
    else:
        return fact(n)+sum_of_series(n-1)

print("Sum of series is:", sum_of_series(n))