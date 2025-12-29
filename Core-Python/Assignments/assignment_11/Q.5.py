#5. Python Program to Sort a List According to the Length of the Elements within the list.
n=int(input("Enter elements:"))
arr=[]
for i in range(n):
    val=input("Enter elements:")
    arr.append(val)
print(arr)
arr.sort(key=len)
print(arr)