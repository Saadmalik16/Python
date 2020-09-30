from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod #iska mtlb hay ka is class ko ab jo jo class bbi inherit karay gi usko iskay functions zaroor overwrite krny hain
    def Area(self): #abstract class ka object ni bnta
        return 0

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def Area(self):
        return self.height * self.width

a = int(input("Enter Height of the Rectangle: "))
b = int(input("Enter Width of the Rectangle: "))
rec  = Rectangle(a,b)
print("The Area of the Rectangle is: ", rec.Area())
