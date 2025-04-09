import random  # Import the random module to generate random numbers

def guess(x):
    # Generate a random number between 1 and x
    random_number = random.randint(1, x)
    guess = 0  # Initialize the guess variable to keep track of the user's guess

    # Loop until the guess is correct
    while guess != random_number:
        # Prompt the user to guess a number between 1 and x
        guess = int(input(f'Guess a number between 1 and {x}: '))

        # Check if the guess is too low or too high
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    # Once the correct guess is made, print the success message
    print("Yay! Congratulations, you guessed the correct number! 🎉")

# Call the function to start the game with a range from 1 to 10
guess(10)
