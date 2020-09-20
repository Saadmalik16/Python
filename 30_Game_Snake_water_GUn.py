import  random
print("This is small game: so use and enjoy it!")

n = 1
pc = 0  # score of pc
user = 0  # score of user

while(n <= 3):
    n = n + 1
    choice_user = input(("Enter your choice:\n" "S = Snake\n" "W = water\n" "G = Gun\n"))

    list = ["Snake","Water","Gun"]
    choice_pc = random.choice(list)
    print(choice_pc)

    if choice_user == "S" and choice_pc == "Water":
        user = int(user + 1)
    elif choice_user == "S" and choice_pc == "Gun":
        pc = int(pc + 1)
    elif choice_user == "W" and choice_pc == "Gun":
        user = int(user +1)
    elif choice_user == "W" and choice_pc == "Snake":
        pc = int(pc +1)
    elif choice_user == "G" and choice_pc == "Water":
        pc = int(pc +1)
    elif choice_user == "G" and choice_pc == "snake":
        user = int(user + 1)

print("Score of pc: ", pc)
print("Score of user: ", user)
if pc > user:
    print("Oops! Game over! PC won the game.")
elif user > pc:
    print("Congratulations! You won the game.")
else:
    print("Game Draw!")
