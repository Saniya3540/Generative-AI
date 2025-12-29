# 2. Python Program to Merge Two Lists and Sort it
n1=int(input("Enter elements you want:"))
data1=[]
for i in range(n1):
    val1=int(input("Enter elements:"))
    data1=data1+[val1]
n2=int(input("Enter elements you want:"))
data2=[]
for i in range(n2):
    val2=int(input("Enter elements:"))
    data2=data2+[val2]

data1.extend(data2)
print(data1)
data1.sort()
print(data1)