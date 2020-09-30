class Student:
    leaves = 4 # class variable jitny bi object banay gain sb is variable ko share karain gaay
    def __init__(self,age,sec): #constructor
        self.age = age
        self.sec = sec

    def print_detail(self):
        return f"Age is {self.age}. and Section is {self.sec}"
    #pass # agr python ma kuch na likhna ho then hum wahan simple pass likh detay hain

saad = Student(20, "5B" ) # saad and ahmad are objects here
#ahmad = Student()
print(saad.age)
#
# saad.age = 20 # age or sec yahan instance variable hain
# saad.sec = "5B"
#
# print(saad.sec)
# print(saad.__dict__) #returned dictionary of specifin object
# print(saad.leaves)
# # if we want to change leaves then we will change only with class name
# # because they are class variable not instance
# Student.leaves = 5
# print(Student.leaves)
# print(saad.leaves)

# print(saad.print_detail())