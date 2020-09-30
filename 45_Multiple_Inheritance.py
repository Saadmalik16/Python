class Student:
    no_of_leaves = 4
    def __init__(self, name, reg_no, dept):
        self.name = name
        self.reg = reg_no
        self.dept = dept

    def Student_Detail(self):
        return f"Name of the Student is {self.name}. Registration Number of the Studnet is {self.reg}" \
               f"Department of the Student is {self.dept}"

    @classmethod #for change the value of the variable of the class
    def change (cls, new):
        cls.no_of_leaves = new

    @classmethod #
    def Split (cls, string):
        return cls(*string.split("-"))

class Gamer:

    def __init__(self, name, game):
        self.name = name
        self.game = game


    def Gamer_detail(self):
        return f"The Name of the Gamer is {self.name}. Specialist is {self.game}"

class Programmer(Student,Gamer): #oreder ka hisaab sa constructor or variable use hoon gaay
    lang = "PYTHON"
    def Language(self):
        print(self.lang)

saad = Student("Saad Ahmad", "0067", "BSCS" )
ahmad = Student.Split("Saad Ahmad-0067-BSCS")
sam = Gamer("Sam Malik", "PUBG")
#saad.change(10)
# print(saad.no_of_leaves)
# print(ahmad.dept)
# print(saad.Student_Detail())
#print(sam.Gamer_detail())