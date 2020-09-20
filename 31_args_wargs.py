# def func_name(a,b,c,d):
#     print(a,b,c,d)
# func_name("Saad", "Ahmad", "Dawood", "Shahzaib")
# agr kaal ko hum or name add akrain tw hamain function ma b changing krni pry gi sth sth har baar
def funarg(normal , *args , **kwargs): #this order very important
    print(normal)
    for item in args:
        print(item)
    print("\nI would like to introduce: ")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
normal = "My name is Saad"
arg = ["Saad","Ahmad", "Dawood", "Shahzaib", "Ahmad", "Dawood", "Shahzaib"]
kargs = {"Saad":"Programmer", "Shahzaib":"CA", "Dawood":"Police Officer"}
funarg(normal,*arg,**kargs)
