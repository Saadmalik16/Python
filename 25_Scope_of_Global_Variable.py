# a = 5 # Gloabal variable program ka andr kahin bi use ho skta hay
# def func1(b):
#     #a = 10 # local variable jo sirf is function ma chalay ga
#     global a
#     a = a + 5
#     print(a)
#     print(b, "Okay we Save it")
# func1("I am Saad Ahmad")
# print(a)

a = 12
def saad():
    a = 10
    def ahmad():
        global a
        a = 50
        ahmad()
        print("The Value of a is ahmad() ", a)
saad()
#print(a)