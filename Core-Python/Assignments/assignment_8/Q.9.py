#Q.9. Write a program to check if entered number is a palindrome or not.
def rev_of_num(num):
    rev=0
    while num!=0:
        r=num%10
        rev=rev*10+r
        num=num//10
    return rev
num=int(input("Enter number:"))
if num==rev_of_num(num):
    print(num,"is a Palindrome")
else:
    print(num,"is not a Palindrome")