#Q.11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def count_digits(num):
    count = 0
    temp = num
    while temp != 0:
        temp //= 10
        count += 1
    return count

def is_armstrong(num):
    n = count_digits(num)  
    total = 0
    temp = num
    while temp != 0:
        digit = temp % 10
        total += digit ** n
        temp //= 10
    return total == num 

num = int(input("Enter the number: "))
if is_armstrong(num):
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")
