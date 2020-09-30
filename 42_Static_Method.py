# @classmethod hum use karain tw automatically self object ya class as an argument pass hoti hay
# magar hamain agar ya ni krna simple method sa kaam krna tw staticc method use karain gay class
class Student:
    leaves = 4 # class variable jitny bi object banay gain sb is variable ko share karain gaay
    def __init__(self,age,sec): #constructor
        self.age = age
        self.sec = sec

    @classmethod
    def change_leave(cls, new):
        cls.leaves = new

    @classmethod
    def from_str(cls, string):
        #a = string.split("-")
        #return cls(a[0], a[1])
        return cls(*string.split("-"))

    @staticmethod
    def print(string):
        print("Your Name is : " + string)

saad = Student(20, "5B" )
ahmad = Student.from_str("19-5C")
# saad.change_leave(10)
# print(saad.leaves)
# print(ahmad.sec)
saad.print("Saad")