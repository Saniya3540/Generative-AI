#12. Python Program to count number of lowercase characters in a string.
s=input("Enter a String:")
count=0
for ch in s:
    if ch.islower():
        count+=1
print(count)