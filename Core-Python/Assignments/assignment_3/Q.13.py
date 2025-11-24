#Q.13. Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill
unit=float(input("Enter electricity unit:"))
amount=0
if unit<=50:
    amount=0.5*unit
elif unit<=150:
    amount=(50*0.5)+(unit-50)*0.75
elif unit<=250:
    amount=(50*0.5)+(100*0.75)+(unit-150)*1.2
else: 
    amount=(50*0.5)+(100*0.75)+(100*1.2)+(unit-250)*1.5
Total_bill=amount+(0.2*amount)
print("Electricity Bill is :",Total_bill)