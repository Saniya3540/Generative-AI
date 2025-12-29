#9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String
s=input("Enter a String:")
char_count=0
word_count=0
for x in s:
    if x!=" ":
        char_count+=1
words=s.split()
word_count=len(words)
print("Number of characters:", char_count)
print("Number of words:", word_count)