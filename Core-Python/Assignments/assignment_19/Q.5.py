#5. Find all of the words in a string that are less than 5 letters (take input from user)
text=input("Enter String:")
words=[w for w in text.split() if len(w) < 5]
print(words)