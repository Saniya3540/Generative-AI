#5. Python Program to Count the Number of Vowels in a String
s=input("Enter a String:")
vowels="aeiou"
count=0
for x in s:
    if x.lower() in vowels:
         count+=1
print(count)