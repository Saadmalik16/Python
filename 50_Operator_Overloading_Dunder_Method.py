class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def __repr__(self): #dunder method
        return f"Employee('{self.name}', '{self.role}', {self.salary})"

    def __str__(self):
        return f"The Name of the Employee is {self.name} Role of the Employee is {self.role} and Salary is {self.salary}"

    def __add__(self, other): #Mapping operators in function
        return self.salary - other.salary

    def __truediv__(self, other):
        return self.salary / other.salary


emp1 = Employee("Saad Ahmad", "CEO", 5000)
emp2 = Employee("Sam Ahmad", "Director", 3000)

print(emp1 + emp2)
print(repr(emp1),"\n",emp2)