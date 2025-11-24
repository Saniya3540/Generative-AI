#Q.g.
for i in range(1,6):
    for j in range(1,6-i):
      print(" ",end=" ")
    ch='A'
    for j in range(2*i-1):
       print(ch,end=" ")
       ch=chr(ord(ch)+1)
    print()