#7. Find the sum of three-digit number.
num=int(input("Enter 3 digit number:"))
sum=0
sum=num%10
num=num//10
sum+=num%10
num=num//10
sum+=num%10
num=num//10
print("Sum is:",sum)
