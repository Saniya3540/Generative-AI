#2. Python Program to Concatenate Two Dictionaries Into One
data1={}
key=int(input("Enter Key:"))
values=input("Enter Values:")
data1[key]=values
print(data1)

data2={}
key=int(input("Enter Key:"))
values=input("Enter Values:")
data2[key]=values
print(data2)

data1.update(data2)
print("Concatenate Dict:",data1)