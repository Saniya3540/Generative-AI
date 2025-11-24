#Q.7. Write a program to print first n prime numbers.
num=int(input("Enter how many prime number do you want:"))
count=0
i=2
while count<num:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        count+=1
    i+=1