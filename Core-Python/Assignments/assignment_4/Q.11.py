#Q.11. WAP to check if given number Strong Number.
num=int(input("Enter Number:"))
temp=num
sum=0
while num>0:
   r=num%10
   fact=1
   for i in range(1,r+1):
    fact=fact*i
   sum+=fact
   num=num//10
if sum==temp:
   print(temp,"is a Strong Number")
else:
   print(temp,"is not a Strong Number")