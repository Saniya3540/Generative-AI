#9. Write a program to create three lists of numbers, their squares and cubes
n=int(input("Enter elements you want:"))
data=[]
squares=[]
cubes=[]

for i in range(n):
    val=int(input("Enter elements:"))
    data.append(val)
    squares.append(val**2)
    cubes.append(val**3)

print(data)
print("Square list:",squares)
print("Cubes:",cubes)