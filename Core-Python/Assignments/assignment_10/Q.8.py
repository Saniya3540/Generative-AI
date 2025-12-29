#8. Write a program to create a duplicate of an existing arr. It should not point to same arr.
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    val = int(input("Enter element: "))
    arr = arr + [val]

duplicate_arr = []
for i in arr:
    duplicate_arr = duplicate_arr + [i]

print("Original arr:", arr)
print("Duplicate arr:", duplicate_arr)
