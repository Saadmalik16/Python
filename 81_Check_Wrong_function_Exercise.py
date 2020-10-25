import random

def Multiplication(a):
    result = []
    for i in range(1,6):
        mul = f"{a} * {i} = {a*i}"
        result.append(mul)
    #print(result)
    mul2 = f"{a} * {6} = {random.randint(a*5, a*8)}"
    result.append(mul2)
    #print(result)
    for j in range(7,11):
        mul3 = f"{a} * {j} = {a*j}"
        result.append(mul3)
    return (result)

def CheckMul(b):
    result2 = []
    for k in range(1,11):
        mul4 = f"{b} * {k} = {b*k}"
        result2.append(mul4)
    return (result2)

if __name__ == '__main__':
    c = int(input("Enter Any Number: "))
    d = Multiplication(c)
    e = CheckMul(c)
    print(d)
    print(e)
