#8. Print 1 to 100 in snakes and ladder pattern.
n=list(range(1,101))
index=0
for i in range(10):
    data=n[index:index+10]
    if i%2==1:
        data.reverse()
    print(data)
    index+=10