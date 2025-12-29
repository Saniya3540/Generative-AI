#14. Python Program to count the occurrences of each word in a string.
text = input("Enter a string: ")
words = text.split()  
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1  
print(word_count)
