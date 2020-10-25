Lays = 50
Nestle_Juice = 50
Coke = 100
Sprite = 90

a = int(input("What do you want: "))
b = int(input("How many you want: "))
c = int(input("Rupees: "))
d = c - (a*b)
print(f"You buy {a} in {b} Quantity ")
print(f"You Paid {c} Amount and Remaining Amount is {d} ")
