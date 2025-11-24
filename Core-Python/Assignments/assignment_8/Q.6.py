#Q.6. Write a program to find print the following Fibonacci series using functions: (1 1 2 3 5 8 n terms)
def fibo(n):
    a,b=1,1
    for i in range(1,n+1):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
n=int(input("Enter n:"))
print("Fibonacci Series is:",end="")
fibo(n)