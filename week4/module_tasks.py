# Activity 1: Importing Modules

import random

print("Please enter the minimum value:")
min = int(input())
print("Please enter the maximum value:")
max = int(input())
rand = random.randrange(min, max)
print(f"I am thinking of a number between {min} and {max}. Can you guess what it is?")

for i in range(min, max):
    guess = int(input())
    if guess > rand:
        print("Your guess is too high.")
        print("Try again!")
    elif guess < rand:
        print("Your guess is too low.")
        print("Try again!")
    else:
        print("Congratulations! You guessed my number!")
        break





