#4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
n=int(input("Enter number: "))
data={}
for x in range(1,n+1):
    data[x]=x*x
print(data)