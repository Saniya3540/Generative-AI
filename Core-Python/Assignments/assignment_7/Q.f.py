#Q.f
for i in range(1,6):
    for j in range(1,7-i):
        if  i==1 : 
         print(j,end=" ")
        else:
            if j==1:
             print(i,end=" ")
            elif  j==6-i:
                print(5,end=" ")
            else:
                print(" ",end=" ")
    print()