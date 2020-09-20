# l1 = ["1","2","3","4","5"]
# for i in range(len(l1)):
#     l1[i] = int(l1[i])
# l1[2] = l1[2] + 10
# print(l1[2])
def square(a):
    return a*a
def cube(a):
    return a*a*a
def greater(a):
    return a>5
#function = (square,cube)
number = [1,2,3,4,5,6,7,8,9,0]
# #list2 = list(map(lambda x: x*x, number))
# number = list(map(int,number))
# number[2] = number[2] + 10
# print(number[2])
# for i in number:
#     number2 = list(map(lambda x:x(i), function))
#     print(number2)
# number2 = list(filter(greater,number))
# print(number2)

from functools import reduce
# num = 0
# for i in number:
#     num = num + i
num = reduce(lambda x,y:x+y, number)
print(num)
