#4. Remove all of the vowels in a string (take input from user)
text=input("Enter String:")
result=''.join(ch for ch in text if ch.lower() not in 'aeiou')
print(result)