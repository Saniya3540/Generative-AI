#6. Python Program to Multiply All the Items in a Dictionary
n=int(input("Enter no:"))
data={}
for i in range(n):
    key=int(input("Enter Key:"))
    value=int(input("Enter Value:"))
    data[key]=value
result=1
for  x in data.values():
    result=result*x
print(data)
print(result)