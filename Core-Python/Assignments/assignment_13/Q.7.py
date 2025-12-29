#7. Python Program to Remove the Given Key from a Dictionary
n=int(input("Enter no:"))
data={}
for i in range(n):
    key=int(input("Enter Key:"))
    value=int(input("Enter Value:"))
    data[key]=value
print(data)
s=int(input("Enter search key:"))
if s in data.keys():
    del data[s]
else:
    print("Key not found")
print("Updated Dict:",data)