#Q.4. Sum of all odd numbers between 1 to n
def odd_num(n):
    total=0
    for i in range(1,n+1):
        if i%2!=0:
            total+=i
    return total
           
n=int(input("Enter n:"))
print("sum of odd number:",odd_num(n))