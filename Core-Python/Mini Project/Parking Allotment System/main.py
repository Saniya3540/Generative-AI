from parking_system import ParkingSystem

ps=ParkingSystem()
choice=0

while choice!=4:
    try:
        print("\n------Parking Management System------")
        print("1. Show Slots")
        print("2. Park Car")
        print("3. Unpark Car")
        print("4. Exit")

        choice=int(input("Enter your choice:"))

        if choice==1:
            ps.showSlots()

        elif choice==2:
            ps.parkCar()

        elif choice==3:
            slot=int(input("Enter slot number:"))
            ps.unparkCar(slot)

        elif choice==4:
            ps.saveData()
            print("Exit!!!")

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter numbers only")
