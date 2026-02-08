'''Write a program to
1. create a package “SY” which has class SYMARKS (Computer Total,
MathsTotal, ElectronicsTotal).'''

class SYMarks:
    def __init__(self, computer, maths, electronics):
        self.ComputerTotal = computer
        self.MathsTotal = maths
        self.ElectronicsTotal = electronics
