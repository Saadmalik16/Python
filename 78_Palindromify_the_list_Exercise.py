def Palindrome(a):
    return str(a) == str(a)[::-1]

def Next_Palimdrome(b):
    if b>10:
        b = b + 1
        while not Palindrome(b):
            b += 1
        return b
    else:
        return b

if __name__ == '__main__':
    list=[]
    size = int(input("Enter the Size of List: "))
    for i in range(size):
        number = int(input("Enter the Value: "))
        list.append(number)

    for i in range(size):
        print(f"Next Palindrome {list[i]} is {Next_Palimdrome(list[i])}")