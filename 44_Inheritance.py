class Student:
    leaves = 4 # class variable jitny bi object banay gain sb is variable ko share karain gaay
    def __init__(self,age,sec): #constructor
        self.age = age
        self.sec = sec
    def printStd(self):
        return f"The Student Name is  {self.age} . and Student Section is {self.sec}"

class Programmer(Student):
    def __init__(self, age , sec , language):
        self.age = age
        self.sec = sec
        self.language = language

    def printprog(self):
        return f"The Programmer Age is  {self.age} . and Programmer Section is {self.sec} . Language are {self.language}"



saad = Student(20, "5B" )
ahmad = Student(19, "5C")
bro = Programmer(21,"5C" , ["Python", "C++"])
print(bro.printprog())
print(bro.printStd())
# saad.change_leave(10)
# print(saad.leaves)
# print(ahmad.sec)
