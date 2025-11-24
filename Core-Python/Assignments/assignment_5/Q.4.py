#Q.4. Write a program to check if given number is Armstrong number or not. (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +4*4*4*4)
num=int(input("Enter the number:"))
temp=num
sum=0
count=0
while num!=0:
    sum=sum+(num%10)
    num=num//10
    count+=1
print("Count is:",count)
num=temp
total=0
while num!=0:
    total=total+(num%10)**count
    num=num//10
print("Total=",total)
if total==temp:
    print(temp,"is Armstrong Number")
else:
    print(temp,"is not Armstrong Number")
