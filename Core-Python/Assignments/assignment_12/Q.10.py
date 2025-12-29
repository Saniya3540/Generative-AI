#10.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
s1=input("Enter First String:")
s2=input("Enter Second String:")
len1=0
len2=0
for _ in s1:
    len1+=1
for _ in s2:
    len2+=1

if len1>len2:
    print(s1)
else:
    print(s2)