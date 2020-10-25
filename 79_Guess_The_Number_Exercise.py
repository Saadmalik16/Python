import random
print("Welcome to the Guess Number Game")
print("Player 1 Select the Number and Player 2 Guess the Selected Number")
Name1 = input("Enter Player 1 Name: ")
Name2 = input("Enter Player 2 Name: ")
Player1 = 0
Player2 = 0

#Actual_Number = 50
Chances = 1
Min_Range = int(input(f"Player 1 {Name1} Enter the Minimum Range: "))
Max_Range = int(input(f"Player 1 {Name1} Enter the Maximum Range: "))
Actual_Number = random.randint(Min_Range,Max_Range)
print(f"Player 2 {Name2} You Have only 5 Chances to Guess the Number. ")

while Chances<=5:
    Guess_Number = int(input(f"Player 2 {Name2} Guess the Actual Number between {Min_Range} to {Max_Range}: "))
    if Guess_Number < Actual_Number:
        print(f"Player 2 {Name2} Your Number is smaller then Actual Number")
        Chances = Chances + 1
    elif Guess_Number > Actual_Number:
        print(f"Player 2 {Name2} Your Number is Greater then Actual Number")
        Chances = Chances + 1
    else:
        print(f"Player 2 {Name2} You take {Chances} Chances to Guess the Number")
        print(f"Player 2 {Name2} Congratulation You Choose the Right Number {Guess_Number}")
        print(f"Player 1 {Name1} You Lose You Player 2 Guess Your Number Number {Guess_Number}")
        Player2 = Player2 + 1
        print(f"Player2 {Name2} has {Player2} Points")
        print(f"Player1 {Name1} has {Player1} Points")
        break
if Chances>5:
    print(f"Game Over You Lose Player 2 {Name2} ")
    print(f"The Actual Number is {Actual_Number}")
    Player1 = Player1 + 1
    print(f"Player1 {Name1} has {Player1} Points")
    print(f"Player2 {Name2} has {Player2} Points")

#For Player Two

print(f"Player 2 {Name2} Select the Number and Player 1 {Name1} Guess the Selected Number")

#Actual_Number = 50
Chances2 = 1
Min_Range2 = int(input(f"Player 2 {Name2} Enter the Minimum Range: "))
Max_Range2 = int(input(f"Player 2 {Name1} Enter the Maximum Range: "))
Actual_Number2 = random.randint(Min_Range2, Max_Range2)
print(f"Player 1 {Name1} You Have only 5 Chances to Guess the Number. ")

while Chances2<=5:
    Guess_Number2 = int(input(f"Player 1 {Name1} Guess the Actual Number between {Min_Range2} to {Max_Range2}: "))
    if Guess_Number2 < Actual_Number2:
        print(f"Player 1 {Name1} Your Number is smaller then Actual Number")
        Chances2 = Chances2 + 1
    elif Guess_Number2 > Actual_Number2:
        print(f"Player 1 {Name1} Your Number is Greater then Actual Number")
        Chances2 = Chances2 + 1
    else:
        print(f"Player 1 {Name1} You take {Chances} Chances to Guess the Number")
        print(f"Player 1 {Name1} Congratulation You Choose the Right Number {Guess_Number2}")
        print(f"Player 2 {Name2} You Lose You Player 1 Guess Your Number Number {Guess_Number2}")
        print(f"Player1 {Name1} has {Player1} Points")
        print(f"Player2 {Name2} has{Player2} Points")
        break
if Chances2>5:
    print(f"Game Over You Lose Player 1 {Name1} ")
    print(f"The Actual Number is {Actual_Number2}")
    Player2 = Player2 + 1
    print(f"Player2 {Name2} has {Player2} Points")
    print(f"Player1 {Name1} has {Player1} Points")

