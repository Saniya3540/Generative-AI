#Q.6. Write a program to calculate profit or loss.
SP=float(input("Enter the Selling Price:"))
CP=float(input("Enter Cost Price:"))
if SP>CP:
    print("Profit=",SP-CP)
elif CP>SP:
    print("Loss=",CP-SP)
else:
    print("No Profit,No Loss!")

