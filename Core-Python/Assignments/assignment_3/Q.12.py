#Q.12. Write a program to check if given 3 digit number is a palindrome or not.
num=int(input("Enter 3 digit number:"))
temp=num
rev=0
rev=rev*10+num%10
num=num//10
rev=rev*10+num%10
num=num//10
rev=rev*10+num%10
num=num//10
if temp==rev:
    print(temp,"is Palindrome!")
else:
    print(temp,"is not Palindrome!")


