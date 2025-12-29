#6. Write a program to remove duplicates from the arr.
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    val = int(input("Enter element: "))
    arr = arr + [val]

new_arr = []
for i in arr:
    found = False
    for j in new_arr:
        if j == i:
            found = True
            break
    if not found:
        new_arr = new_arr + [i]

print("arr after removing duplicates:", new_arr)
