# PYTHON ROCK PAPER SCISSORS GAME

import random

options = ("rock", "paper", "scissors")

running = True

while True:
    player = None
    computer = random.choice(options)

    while player not in options:    
        player = input("Enter a choice (rock, paper, scissors) : ")

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if(player == computer):
        print("IT'S A TIE!")
    elif player == "rock" and computer == "scissors":
        print("YOU WIN!")
    elif player == "paper" and computer == "rock":
        print("YOU WIN!")
    elif player == "scissors" and computer == "paper":
        print("YOU WIN!")
    else:
        print("YOU LOSE!")

    if not input("Play Again? (y/n) : ").lower() == "y":
        break

print("Thanks for playing!")


 
