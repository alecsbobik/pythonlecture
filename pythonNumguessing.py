# Python Number Guessing Game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    #local var
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses +=1

        # if your guess is out of range
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range.")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        # if your guess is too low
        elif guess < answer:
            print("Too low! Try again!")
        # if your guess is too high
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess.")
        print(f"Please select a number between {lowest_num} and {highest_num}")


# print(answer)