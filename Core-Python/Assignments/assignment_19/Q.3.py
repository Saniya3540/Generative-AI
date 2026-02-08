#3. Count the number of spaces in a string (take input from user)
text=input("Enter String:")
count=sum(1 for ch in text if ch==' ')
print("Spaces:", count)