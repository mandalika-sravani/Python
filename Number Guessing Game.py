# PYTHON NUMBER GUESSING GAME

import random

low_num = 1
high_num = 100

answer = random.randint(low_num, high_num)

guesses = 0
is_running = True

print("PYTHON NUMBER GUESSING GAME")
print(f"Select a number between {low_num} and {high_num}")

while is_running:
    guess = input("Enter your guess : ")

    if guess.isdigit():
        guess = int(guess)

        guesses += 1

        if guess < low_num or guess > high_num:
            print("The number is out of range")
            print(f"Please select a number between {low_num} and {high_num}")
        elif guess < answer:
            print("TOO LOW! Try again!")
        elif guess > answer:
            print("TOO HIGH! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses : {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {low_num} and {high_num}")