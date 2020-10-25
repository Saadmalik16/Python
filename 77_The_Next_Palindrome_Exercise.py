def Palindrome(a):
    return str(a) == str(a)[::-1]

def Next_Palindrome(b):
    b = b + 1
    while not Palindrome(b):
        b += 1
    return b

if __name__ == '__main__':
    size = int(input("How many Test cases you take as Input: "))
    list= []

    for i in range(size):
        number=(int(input("Enter list element: ")))
        list.append(number)

    for i in range(size):
        print(f"Next Palindrome of {list[i]} is {Next_Palindrome(list[i])}")
