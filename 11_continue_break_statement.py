"""
i = 1
while(True):
    if i+1<5:
        i = i+1
        continue # current iteration pr focus kro nechay sara profram bhol jao
    print(i+1, end=" ")
    if (i==50):
        break # loop ko choor do loop sa bahir ajao
    i = i + 1
"""
while(True):
    i = int(input("Enter any Number: \n"))
    if i<100:
        print("You Entered Number is in Range... \n")
        break
    else:
        print("You Entered Number is not in Range Please try Again \n")
        continue

