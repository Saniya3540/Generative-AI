#6. Write a program to print Fibonacci series using recursion.
num=int(input("Enter a Number:"))
def fibo(num,a,b):
    if num==0:
        return 
    else:
        c=a+b
        print(c)
        fibo(num-1,b,c)
fibo(num,1,0)