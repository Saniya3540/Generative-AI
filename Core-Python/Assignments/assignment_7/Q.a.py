#Q.a.
for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        if i == j or j == 1:
            print("*", end="   ")
        else:
            print(" ", end="   ")
    print()
i = 5
for j in range(1,6-i):
    print(" ", end=" ")
for j in range(1,i+1):
    if i == j or j == 1:
        print("*", end="   ")
    else:
        print(" ", end="   ")
print()
for i in range(4,0,-1):
    for j in range(1,6-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        if i == j or j == 1:
            print("*", end="   ")
        else:
            print(" ", end="   ")
    print()
