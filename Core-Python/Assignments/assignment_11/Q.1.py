#1. Python Program to Put Even and Odd elements of a List into two Different Lists
n=int(input("Enter elements you want:"))
data=[]
for i in range(n):
    val=int(input("Enter Elements:"))
    data=data+[val]
even_lst=[]
odd_lst=[]
for x in data:
    if x%2==0:
        even_lst.append(x)
    else:
        odd_lst.append(x)

print("Even elements:",even_lst)
print("Odd elements:",odd_lst)
