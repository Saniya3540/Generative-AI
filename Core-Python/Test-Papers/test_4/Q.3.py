r=11
c=22
k=c-1
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1:
            print("*",end="")
        elif j==k or k==23:
            print("*",end="")
        else:
            print(" ",end="")
    k-=2
    print()

