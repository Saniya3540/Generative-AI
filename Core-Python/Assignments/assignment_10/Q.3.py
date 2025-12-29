#3. Write a program to find the second largest element in the data.
n=int(input("Enter number of elements:"))
data=[]

for i in range(n):
    val=int(input("Enter elements:"))
    data=data+[val]

first=data[0]
second=data[0]
for x in data:
    if x>first:
        second=first
        first=x
    elif x>second and x!=first:
        second=x

print("Second Largest Element is:",second)
