#8. Python Program to Remove the Characters of Odd Index Values in a String
s=input("Enter a String:")
result=" "
for i in range(len(s)):
    if i%2==0:
        result+=s[i]
print(result)