#5. Accept a number from user and check if this element is present in the arr or not. Also tell how many times it is present in the arr.
n=int(input("Enter number of elements:"))
arr=[]
count=0
for i in range(n):
    val=int(input("Enter Elements:"))
    arr=arr+[val]
x=int(input("Enter Element to check:"))
for i in arr:
    if i==x:
        count+=1
if count>0:
    print(x,"is Present in arr")
    print("It is present",count,"times")
else:
    print("Element is not present in arr")