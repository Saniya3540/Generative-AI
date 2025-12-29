# 3. Python Program to Sort the List According to the Second Element in Sublist
n = int(input("Enter number of sublists: "))
data = []
for i in range(n):
    num1 = int(input("Enter first element: "))
    num2 = int(input("Enter second element: "))
    data.append([num1,num2])
print("Before sort data:",data)

data.sort(key=lambda x: x[1])
print("Sorted list by second element:", data)