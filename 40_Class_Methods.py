class Student:
    leaves = 4 # class variable jitny bi object banay gain sb is variable ko share karain gaay
    def __init__(self,age,sec): #constructor
        self.age = age
        self.sec = sec

    @classmethod
    def change_leave(cls, new):
        cls.leaves = new
saad = Student(20, "5B" )
saad.change_leave(10)
print(saad.leaves)
