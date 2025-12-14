#5. Write a program to find factorial using recursion.
num=int(input("Enter a number:"))
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
print("Fact is:",fact(num))