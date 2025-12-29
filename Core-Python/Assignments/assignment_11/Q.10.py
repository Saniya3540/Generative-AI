#10. Write a program to print list after removing even numbers.
n=int(input("ENter elements you want:"))
data=[]
for i in range(n):
    val=int(input("Enter elements:"))
    data.append(val)
result=[]
for x in data:
    if x%2!=0:
        result.append(x)
print(result)