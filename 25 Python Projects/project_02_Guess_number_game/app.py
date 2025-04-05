import random  # Import the random module to generate random numbers

# Define a function called guess that takes one argument x
def guess(x):
    # Generate a random number between 1 and x (inclusive)
    random_number = random.randint(1, x)
    
    guess = 0  # Initialize the user's guess to 0 (so it doesn't match the random number initially)

    # Keep asking the user to guess until they get it right
    while guess != random_number:
        # Ask the user to guess a number between 1 and x
        guess = int(input(f'Guess a number between 1 and {x}: '))
        
        # Give a hint if the guess is too low
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        # Give a hint if the guess is too high
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    # If the loop ends, it means the user guessed correctly
    print("Yay! Congratulations, you guessed the correct number! 🎉")

# Call the function with 10 as the maximum number
guess(10)
