#7. Write a program to create a new arr from existing arr which contains cube of each number of arr.
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    val = int(input("Enter element: "))
    arr = arr + [val]

cube_arr = []
for i in arr:
    cube_arr = cube_arr + [i * i * i]

print("arr with cubes:", cube_arr)
