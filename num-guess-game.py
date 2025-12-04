import random

secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")

num=int(input("Guess a number between 1 and 100: "))
while num != secret_number:
    if num < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    num = int(input("Guess a number between 1 and 100: "))
print("Congratulations! You've guessed the correct number:", secret_number)
    