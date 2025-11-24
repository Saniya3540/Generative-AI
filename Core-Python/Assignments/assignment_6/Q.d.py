#Q.d.
k=1
for i in range(1,6):
    ch='A'
    for j in range(1,i+1):
      print(ch,end=" ")
      ch=chr(ord(ch)+1)
    print()
