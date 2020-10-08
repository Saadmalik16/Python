class Library:

    # def __init__(self):
    #      self.Library_name = "Saad Library"
    #      self.list_of_books = ["English", "Urdu", "Math", "Physics", "Chemistry"]

    def Library_name(self):
        self.Library_name = "Saad Library"
        return f"Welcome to {self.Library_name}"

    def books(self):
        self.list_of_books = ["English", "Urdu", "Math", "Physics", "Chemistry"]
        return f"We have the Followings Books {self.list_of_books}"

    def lend_book(self):
        self.a = input("Enter Your Name: ")
        self.b = input("Enter the Name of the Book You Want: ")
        return (f"Your Name is {self.a} and you pick {self.b} book. "
                f"Hope You Enjoy Your Service See you Next time")

    def add_book(self):
        self.c = input("Enter the Name of the Book You Want to add: ")
        return (f"Thanks for Donate this Book {self.c}")

    def return_book(self):
        self.d = input("Enter Your Name: ")
        self.e = input("Enter the Name of the Book You Want to Return: ")
        return(f"Your Name is {self.d} and you Return {self.e} book. "
               f"Hope You Enjoy Your Service See you Next time")



z = Library()
print(z.Library_name())
f = int(input("Hello Good Noon Sir .. \n"
      "Press 1 for Display Books \n"
      "Press 2 for Lend Books \n"
      "Press 3 for Add Books \n"
      "Press 4 for Return Books \n"
      "Press 5 for Exit \n"))

while (f is not 5):
    if f == 1:
        print(z.books())
    elif f == 2:
        print(z.lend_book())
    elif f == 3:
        print(z.add_book())
    elif f == 4:
        print(z.return_book())
    else:
        print("Good Bye .... Have a Nice Day")
