#8. Write a program to check whether a number is prime or not using recursion.
num=int(input("Enter a number:"))
def prime_no(num,i=2):
    if num<=1:
        return "Not Prime"
    if i==num:
        return "Prime"
    if num%i==0:
        return "Not Prime"
    return prime_no(num,i+1)

print(prime_no(num))      