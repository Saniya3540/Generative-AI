#Q.7.Write a program to find sum of digits of a number.
def sum_of_digits(num):
    sum=0
    while num!=0:
        sum=sum+(num%10)
        num=num//10
    return sum
num=int(input("Enter number:"))
print("Sum of Digits is:",sum_of_digits(num))
    