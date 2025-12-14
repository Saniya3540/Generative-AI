#7. Write a program to find sum of digits using recursion.
num=int(input("Enter a number:"))
def sum_digits(num):
    if num==0:
        return 0
    return (num%10) + sum_digits(num//10)

print("Sum of Digits:",sum_digits(num))
