#2. Write a program to find maximum and minimum element in a data.
n=int(input("Enter number of Elements:"))
data=[]
for i in range(n):
    val=int(input("Enter Elements:"))
    data=data+[val]

max=data[0]
min=data[0]

for  x in data:
        if x>max:
             max=x
        if x<min:
             min=x

print("Maximum element is:",max)
print("Minimum element is:",min)