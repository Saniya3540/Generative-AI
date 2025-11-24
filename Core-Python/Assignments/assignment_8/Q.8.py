#Q.8. Write a program find reverse of a number
def rev_of_num(num):
    rev=0
    while num!=0:
        r=num%10
        rev=rev*10+r
        num=num//10
    return rev
num=int(input("Enter number:"))
print("Reverse number is:",rev_of_num(num))