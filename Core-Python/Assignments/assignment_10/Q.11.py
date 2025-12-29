#11. Write a program to print all numbers which are divisible by m and n in the list.
n = int(input("Enter number of elements: "))
data = []
for i in range(n):
    val = int(input("Enter element: "))
    data = data + [val]

m = int(input("Enter value of m: "))
p = int(input("Enter value of n: "))

divisible_list = []
for i in data:
    if i % m == 0 and i % p == 0:
        divisible_list = divisible_list + [i]

print("Numbers divisible by both m and n:", divisible_list)
