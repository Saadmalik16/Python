def dec(func):
    def dec2():
        print("Hye Boy")
        func
        print("Okay okay")
    return dec2()
#@dec1
def dec3():
    print("I am Saad")

dec3 = dec(dec3())
print(dec3)