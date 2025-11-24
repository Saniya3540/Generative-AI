#5. WAP to calculate selling price of book based on cost price and discount.
CP=float(input("Cost Price of book is:"))
dis=float(input("Discount on book is:"))
SP=CP- (CP*(dis/100))
print("Selling Price of book is:",SP)