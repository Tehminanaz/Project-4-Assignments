import random

def guess(x):
    random_number = random.randint(1, x)  # Generate a random number between 1 and x
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))  # Fixed input prompt
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print("Yay! Congratulations, you guessed the correct number! 🎉")

guess(10)