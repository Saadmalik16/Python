a = int(input("Numbers of Apple Provided by Harry's Friends: "))
b = int(input("Minimum Range of Students: "))
c = int(input("Maximum Range of Students: "))
print("\nDisplay Given Range is Divisor or not.")

for i in range(b,c+1):
    if a%i==0:
        print(f"{i} is a divisor of {a}")
    else:
        print(f"{i} is not a divisor of {a}")

