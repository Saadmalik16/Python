# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
#
# if a ==0 or b == 0: #built in raise error
#     raise ZeroDivisionError("A or b Must be a Number not 0") #
# # elif a.isnumeric(): #general raise error
# #     raise Exception("Numbe is ")
#
# print(f"Answer is {a/b}")

a = input("Enter Your Name: ")
try:
    print(b)
except Exception as c:
    if a == "Saad":
        raise ValueError("Saad is Blocked He is not allowed")
print("Exception Handling")