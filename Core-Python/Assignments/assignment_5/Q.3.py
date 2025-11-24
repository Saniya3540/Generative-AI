#Q.3. Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition :
  #a. Children below 12 = 30% discount
  #b. Senior citizen (above 59) = 50% discount
  #c. Others need to pay full.
num=int(input("Enter number of passengers for travelling:"))
Ticket_cost=float(input("Enter the ticket cost:"))
Total=0
count=1
while count<=num:
    age=int(input("Enter the age:"))
    if age<12:
       final_cost=Ticket_cost-(Ticket_cost*30)/100 
       print("Ticket_cost is:",final_cost)
    elif age>59:
        final_cost=Ticket_cost-(Ticket_cost*50)/100 
        print("Ticket_cost is:",final_cost)     
    else:
        final_cost=Ticket_cost
        print("Ticket_cost is:",final_cost)
    Total+=final_cost
    count+=1
print("Total cost of travelling is:",Total)

