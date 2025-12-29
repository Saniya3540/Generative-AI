#10. Write a program to remove all occurrences of a given element in the arr.
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    val = int(input("Enter element: "))
    arr = arr + [val]

x = int(input("Enter element to remove: "))
new_arr = []
for i in arr:
    if i != x:
        new_arr = new_arr + [i]

print("arr after removing element:", new_arr)
