#2. Python Program to Remove the nth Index Character from a Non-Empty String
s=input("Enter a String:")
n=int(input("Enter index:"))
result=s[:n]+s[n+1:]
print(result)