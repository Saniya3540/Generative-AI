from parking import ParkingSlot
from datetime import datetime
import pickle

class ParkingSystem:
    def __init__(self):
        try:
            fp=open("parking.bin","rb")
            self.slots=pickle.load(fp)
            fp.close()
        except:
            self.createSlots()

    def createSlots(self):
        self.slots={}
        for i in range(1,11):
            self.slots[i]=ParkingSlot(i)

    def showSlots(self):
        print("\nSlot   \t Status    \tEntry Time")

        for s in self.slots.values():
            if s.status==1:
                status="Available"
                entry_time="-"
            else:
                status="Occupied"
                entry_time=s.entry_time
            print(s.slot_no,"\t",status,"\t",entry_time)

    def parkCar(self):
                for s in self.slots.values():
                     if s.status==1:
                        s.status=0
                        s.entry_time=datetime.now()
                        print("Car parked in slot:", s.slot_no)
                        print("Entry Time:", s.entry_time)
                        self.saveData()
                        return
                print("No Parking Slot Available")

    def unparkCar(self,slot_no):
        if slot_no not in self.slots:
              print("Invalid Slot Number")
              return
        slot=self.slots[slot_no]

        if slot.status==1:
              print("Slot already free")
              return
        exit_time=datetime.now()
        hours=(exit_time-slot.entry_time).total_seconds()/3600
        hours=int(hours)+1

        bill=self.calculateBill(hours)

        print("Entry Time:",slot.entry_time)
        print("Exit Time:",exit_time)
        print("Total Hours:",hours)
        print("Parking Charge = ₹",bill)

        slot.status=1
        slot.entry_time=None
        self.saveData()

    def calculateBill(self,hours):
         if hours<=4:
              return 50
         else:
              return 50+(hours-4)*20
         
    def saveData(self):
         try:
              fp=open("parking.bin","wb")
              pickle.dump(self.slots,fp)
              fp.close()
         except:
              print("Error while Saving Data")
