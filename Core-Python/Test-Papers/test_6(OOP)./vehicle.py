from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,persons):
        self.persons=persons

    @abstractmethod
    def cal_toll(self):
        pass

class TwoWheeler(Vehicle):
    def cal_toll(self):
        toll=20
        if self.persons>2:
            toll+=(self.persons-2)*10
        return toll
    
class ThreeWheeler(Vehicle):
    def cal_toll(self):
        toll=30
        if self.persons>3:
            toll+=(self.persons-3)*20
        return toll
    
class FourWheeler(Vehicle):
    def cal_toll(self):
        toll=40
        if self.persons>4:
            toll+=(self.persons-4)*40
        return toll

class HeavyVehicle(Vehicle):
    def cal_toll(self):
        toll=60
        if self.persons>6:
            toll+=(self.persons-6)*100
        return toll