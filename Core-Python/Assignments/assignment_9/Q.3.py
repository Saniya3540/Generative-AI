#3. Write a program to reverse a given number using recursive function.
num=int(input("Enter a Number:"))
def rev(num):
    if num==0:
        return 0
    print(num%10,end="")
    rev(num//10)

rev(num)