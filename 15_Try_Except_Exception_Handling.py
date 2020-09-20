print("Enter 1 Number: ")
num1 = input()
print("Enter 2 Number: ")
num2 = input()

try:
    print("Output is",
          int(num1)+int(num2))
except Exception as e:
    print(e)
print("This Code is very Usefull") #program ma error ho na ho agr koi cheez important hay or apnay print krwani then use try except exception