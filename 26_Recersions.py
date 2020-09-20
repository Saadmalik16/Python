# # # def func1(str1):
# # #     print("This is ", str1)
# # # func1("Saad")
# #
# # n! = n + n-1 + n-2 + n-3 ..... 1
# # n! = n + (n-1)!
#
# def iteration_fact(num):
#     """
#     # Doc String
#     :param num: n! = n + n-1 + n-2 + n-3 ..... 1
#     :return: n! = n + (n-1)!
#     """
#     fac = 1
#     for i in range(num):
#         fac = fac * (i+1)
#     return fac
#
# def recersive_fact(num):
#     """
#     # Doc String
#     :param num: n! = n + n-1 + n-2 + n-3 ..... 1
#     :return: n! = n + (n-1)!
#     """
#     if num == 0:
#         return 1
#     elif num == 1:
#         return 1
#     else:
#         return num * recersive_fact(num-1)
#
# number = int(input("Enter any Number: "))
# print("Iterative Factorial of number is ", iteration_fact(number))
# print("Recersive Factorial of number is ", recersive_fact(number))


def fab(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)
num = int(input("Enter any NUmber: "))
print("Fabonnaci Number", fab(num))