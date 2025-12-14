#2. Write a program to check if given number is Armstrong or not using recursive function.
num=int(input("Enter number:"))
def count(num):
    if num==0:
        return 0
    return 1+ count(num//10)

def Armstrong(num,power):
    if num==0:
        return 0
    digit=num%10
    return (digit**power) +Armstrong(num//10,power)

digits=count(num)
result=Armstrong(num,digits)
if result==num:
    print(result,"is Armstrong Number!")
else:
    print(result,"is not Armstrong Number")