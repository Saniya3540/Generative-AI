#10. Write a program to reverse a number using recursion.
num=int(input("Enter a number:"))
def rev(num):
    if num==0:
        return 0
    print(num%10,end="")
    rev(num//10)

rev(num)