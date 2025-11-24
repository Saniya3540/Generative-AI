#Q.9. WAP to print all numbers in a range divisible by a given number.
num=int(input("Enter a divisor number:"))
n=int(input("Enter the range:"))
for i in range(1,n+1):
    if i%num==0:
     print(i)
