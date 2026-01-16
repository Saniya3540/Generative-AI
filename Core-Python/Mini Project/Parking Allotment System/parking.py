class ParkingSlot:
    def __init__(self,slot_no,status=1,entry_time=None):
        self.slot_no=slot_no
        self.status=status
        self.entry_time=entry_time

    def __str__(self):
        data=str(self.slot_no)+","+str(self.status)+","+str(self.entry_time)
        return data