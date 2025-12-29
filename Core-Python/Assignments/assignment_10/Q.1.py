#1. Write a program to find sum of all elements of arr
n=int(input("Enter number of Elements:"))
arr=[]
sum=0
for i in range(n):
    val=int(input("Enter elements:"))
    arr=arr+[val]
    sum=sum+val
print("Sum is:",sum)
