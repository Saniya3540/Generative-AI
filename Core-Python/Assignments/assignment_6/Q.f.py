#Q.f.
for i in range(1,6):
    for j in range(1,6-i):
      print(" ",end=" ")
    num=1
    for j in range(2*i-1):
      print(num,end=" ")
      num+=1  
    print()