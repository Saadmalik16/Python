a = int(input("Enter your Age or Birth of Year: "))
if a>1950 and a<2020 :
    a = a+100
    print(f"You Will Become 100 Years old on {a}.")
elif a<90 and a>0 :
    a = 100-a
    print(f"After {a} years you become 100")
elif a>2020:
    print("You are not yet born")
elif a>90 and a<1950:
    print("You seem to be oldest person alive")
else:
    print("Something Went wrong")

b = int(input("Enter your Year of birth: "))
if b<1950:
    print("Something Went Wrong")
else:
    c = int(input("Enter the Particular Year you are old at that time: "))
    c = c - b
    print(f"Your Age at that time is {c}")