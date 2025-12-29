#5. Python Program to Sum All the Items/Values in a Dictionary
n=int(input("Enter no:"))
data={}
for i in range(n):
    key=int(input("Enter Key:"))
    value=int(input("Enter Value:"))
    data[key]=value
print(data)
print("Sum of values:", sum(data.values()))