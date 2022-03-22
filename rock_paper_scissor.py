import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors","test"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper:1, scissors: 2
    computer_picked = options[random_number]
    print("Computer picked ", computer_picked + ".")

    if user_input == "rock" and computer_picked == "scissors":
        print("You Won !!")
        user_wins += 1


    elif user_input == "paper" and computer_picked == "rock":
        print("You Won !!")
        user_wins += 1

    else:
        print("You Lost !!")
        computer_wins += 1


print("You Won", user_wins, "times.")
print("The computer won", computer_wins , "times. ")
print("Goodbye !!")






