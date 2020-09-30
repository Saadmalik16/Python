import random
list = [0,1,2,3,4,5,6,7,8,9,10]
r = random.choice(list)
class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}{a}@CodewithSaad.com"

    def Detail(self):
        return f"Studnet Name is {self.fname}{self.lname}"

    @property
    def Email(self):
        if self.fname == None or self.lname == None:
            return "Please Set Your Email First"
        return f"Your Generated Email is : {self.fname}.{self.lname}{r}@CodeWithSaad.com"

    @Email.setter
    def Email(self, string):
        print("Setting Now ......")
        names = string.split("@")[0]
        fname = string.split(".")[0]
        lname = string.split(".")[1]

    @Email.deleter
    def Email(self):
        fname = None
        lname = None

print("Your Email Will be Set as Fname.Sname@CodewithSaad.com")
a = input("Enter First Name: ")
b = input("Enter Second Name: ")
s1 = Student(a,b)
print(s1.Email)
