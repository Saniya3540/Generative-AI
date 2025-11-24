#Q.5. A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST.
P1=float(input("ENter price of 1st product:"))
P2=float(input("ENter price of 2nd product:"))
P3=float(input("ENter price of 3rd product:"))
P4=float(input("ENter price of 4th product:"))
P5=float(input("ENter price of 5th product:"))
total=P1+P2+P3+P4+P5
total_cost=total+(total*(18/100))
print("Total cost is:",total_cost)