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


saad = Student(20, "5B" )
ahmad = Student.from_str("19-5C")
saad.change_leave(10)
print(saad.leaves)
print(ahmad.sec)
