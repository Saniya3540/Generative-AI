#13 . Write a program to print list after removing even numbers.
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    val = int(input("Enter element: "))
    arr = arr + [val]

new_list = []
for i in arr:
    if i % 2 != 0:
        new_list = new_list + [i]

print("List after removing even numbers:", new_list)
