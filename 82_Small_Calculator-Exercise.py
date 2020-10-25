
def Calculator(var1,var2,operator):
    if operator == "+" :
        return var1 + var2
    elif operator == "-" :
        return var1 - var2
    elif operator == "*" :
        return var1 * var2
    elif operator == "/" :
        return var1 / var2
    elif operator == "%" :
        return var1 % var2
    elif operator == "avg" :
        return var1 + var2 / 2
    else:
        return "You Enter Something Wrong .... "

if __name__ == '__main__':

    a = int(input("Enter First Value: "))
    b = int(input("Enter Second Value: "))
    print("Select the Operator + (Addition) , - (Subtraction) , * (Multiplication) , / (Division) , % (Modulus) , avg (Average) ")
    c = input("Enter Operator: ")
    d = Calculator(a,b,c)
    print(f"Answer is {d}")