from vehicle import TwoWheeler,ThreeWheeler,FourWheeler,HeavyVehicle

while True:
    print("\n---Toll Plaza---")
    print("1.Two Wheeler")
    print("2.Three Wheeler")
    print("3.Four Wheeler")
    print("4.Heavy Vehicle")
    print("5.Exit")

    ch=int(input("Enter Choice:"))

    if ch == 5:
        print("Exit")
        break
    
    persons=int(input("Enter no. of persons:"))

    if ch == 1:
        v = TwoWheeler(persons)
    elif ch == 2:
        v = ThreeWheeler(persons)
    elif ch == 3:
        v = FourWheeler(persons)
    elif ch == 4:
        v = HeavyVehicle(persons)
    else:
        print("Invalid choice")
        continue

    print("Total Toll:",v.cal_toll())