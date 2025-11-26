#4.write a program to print pattern
# 10101
# 01010
# 10101
# 01010
# 10101
for i in range(1,6):
    for j in range(1,6):
        print((i+j+1)%2,end=" ")
    print()