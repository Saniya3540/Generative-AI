#9. Write a program of having n number of elements in the data and find out even and odd elements in that data and then create two separate datas which will have even elements and other will have odd elements.
n = int(input("Enter number of elements: "))
data = []
for i in range(n):
    val = int(input("Enter element: "))
    data = data + [val]

even_data = []
odd_data = []
for i in data:
    if i % 2 == 0:
        even_data = even_data + [i]
    else:
        odd_data = odd_data + [i]

print("Even elements:", even_data)
print("Odd elements:", odd_data)
