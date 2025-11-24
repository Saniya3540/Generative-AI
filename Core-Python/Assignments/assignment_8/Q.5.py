#Q.5. Sum of all prime numbers between 1 to n
def prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def sum_of_prime(n):
    total=0
    for i in range(1,n+1):
        if prime(i):
            total+=i
    return total
n=int(input("Enter n:"))
print("SUm of Prime number is:",sum_of_prime(n))