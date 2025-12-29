#4. Write a program to reverse the data.
n=int(input("Enter number of elements:"))
data=[]
for i in range(n):
    val=int(input("Enter Elements:"))
    data=data+[val]
rev=[]
i=n-1
while i>=0:
    rev=rev+[data[i]]
    i=i-1

print("Reversed data:",rev)