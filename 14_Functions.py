a = 1
b = 3
c = sum((a,b))
print(c)

def func1():
    print("Hello YOu are in Function 1")
print(func1())

def func1(a,b):
    print("Hello YOu are in Function 1", a+b)
print(func1(4,5))

def func2(v,f):
    """This is a Functiion which return average of two numbers This is doc string function ki phli line"""
    average = (v+f)/2
    print(average)
    return average
v = int(input("Enter First Number: "))
f = int(input("Enter Second Number: "))
z = func2(v,f)
print(z)
print(func2.__doc__)