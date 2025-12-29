#4. Python Program to Find the Second Largest Number in a List Using Bubble Sort
n=int(input("Enter number of elements:"))
data=[]
for i in range(n):
    num=int(input("Enter number:"))
    data.append(num)
print("Before Sorting:",data)

for i in range(n):
    for j in range(0,n-i-1):
        if data[j]>data[j+1]:
            data[j],data[j+1]=data[j+1],data[j]
print("Sorted list:", data)
print("Second largest number:", data[-2])