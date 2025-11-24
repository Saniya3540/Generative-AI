#Q.5. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount. (Use looping to optimize the problem)
amount=int(input("Enter Amount:"))
notes=[500,200,100,50,20,10,5,1]
count=0
for note in notes:
       if amount>=note:
              num_notes=amount//note
              print(note,":",num_notes)
              count+=num_notes
              amount=amount%note 
print("Minimum number of notes:",count)