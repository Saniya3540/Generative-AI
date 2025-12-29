#6. Python Program to Find the Union of two Lists
n1=int(input("Enter the numbers:"))
data1=[]
for i in range(n1):
    val=input("Enter elements:")
    data1.append(val)

n2=int(input("Enter the numbers:"))
data2=[]
for i in range(n2):
    val=input("Enter elements:")
    data2.append(val)

print(data1)
print(data2)

data=list(set(data1).union(set(data2)))
print(data)