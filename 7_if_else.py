a = 10
b = 20
print("Enter Any Number to Check Greater or Smaller: ")
c = int(input())

if c>b:
    print("Greater Number") #indentation automatically give tab or four spaces at start
elif c==b: # If single if use then it check all if conditions if use elif then it can check only particular situation
    print("Numbers are Equal")
else:
    print("Smaller Number")

