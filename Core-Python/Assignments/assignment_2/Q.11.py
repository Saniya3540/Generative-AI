#11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
amount = int(input("Enter the amount: "))
notes = [2000, 500, 100, 50, 20, 10, 5,1]

print("Minimum number of notes needed:")
for note in notes:
    num_notes = amount // note
    amount = amount % note
    if num_notes > 0:
        print(note, ":", num_notes)