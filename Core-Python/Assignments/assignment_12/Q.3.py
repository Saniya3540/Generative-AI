#3. Python Program to Detect if Two Strings are Anagrams
s1=input("Enter first String:")
s2=input("Enter second String:")
if sorted(s1)==sorted(s2):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")