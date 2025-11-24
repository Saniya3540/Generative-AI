#Q.12. WAP to print Armstrong numbers within a given range.
start = int(input("Enter Start of range: "))
end = int(input("Enter End of range: "))
for num in range(start, end+1):
    temp = num
    count = 0
    n = num
    while n > 0:
        count += 1
        n //= 10
    n = num
    s = 0
    while n > 0:
        digit = n % 10
        s += digit ** count
        n //= 10
    if s == temp:
        print(temp)