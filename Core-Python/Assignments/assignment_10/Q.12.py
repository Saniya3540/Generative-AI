#12. Write a program to create three lists of numbers, their squares and cubes
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    val = int(input("Enter element: "))
    arr = arr + [val]

square_list = []
cube_list = []
for i in arr:
    square_list = square_list + [i * i]
    cube_list = cube_list + [i * i * i]

print("Numbers:", arr)
print("Squares:", square_list)
print("Cubes:", cube_list)
