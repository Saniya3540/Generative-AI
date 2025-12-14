#9. Write a program to calculate the m to the power n using recursion.
m=int(input("Enter the base:"))
n=int(input("Enter the power:"))
def ans(m,n):
    if n==0:
        return 1
    return m* ans(m,n-1)

print("Calculation is:",ans(m,n))