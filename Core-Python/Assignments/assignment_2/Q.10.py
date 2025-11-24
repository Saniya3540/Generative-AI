#10. Write a program to reverse three-digit number.
num=int(input("Enter 3 digit number:"))
rev=0
rev=rev*10+num%10
num=num//10
rev=rev*10+num%10
num=num//10
rev=rev*10+num%10
num=num//10
print("Reverse is:",rev)