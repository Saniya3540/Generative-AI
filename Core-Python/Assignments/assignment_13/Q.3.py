#3. Python Program to Check if a Given Key Exists in a Dictionary or Not
data={101, "AAA", 102, "BBB", 103,"CCC"}
print(data)
check_key=int(input("Enter key:"))
if check_key in data:
    print("Key Exist")
else:
    print("Key not found")