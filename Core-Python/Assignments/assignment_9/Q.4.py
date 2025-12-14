#4. Write a program to find sum of n numbers using recursion.
num=int(input("Enter a number:"))
def sum(num):
    if num==0:
        return 0
    return (num%10)+sum(num//10)

print("Sum is:",sum(num))