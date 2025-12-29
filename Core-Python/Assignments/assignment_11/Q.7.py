#7. Python Program to Find the Intersection of Two Lists
n1=int(input("Enter elements:"))
data1=[]
for i in range(n1):
    val=input("Enter Elements:")
    data1=data1+[val]
print(data1)

n2=int(input("Enter elements:"))
data2=[]
for i in range(n2):
    val=input("Enter Elements:")
    data2=data2+[val]
print(data2)

data=list(set(data1).intersection(set(data2)))
print(data)