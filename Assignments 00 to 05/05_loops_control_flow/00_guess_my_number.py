# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

# add a counter to track how many attempts the user took
import random

def main():
    # Generate a random number
    secret_number = random.randint(0, 99)

    print("I am thinking of a number between 0 and 99...")

    # Initialize guess counter
    attempts = 0

    # Get the user's first guess
    guess = int(input("Enter a guess: "))
    attempts += 1

    # Continue looping until the guess matches the secret number
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        # Prompt for another guess
        guess = int(input("Enter a new number: "))
        attempts += 1

    # Congratulate the user and show the number of attempts
    print(f"Congrats! The number was: {secret_number}")
    print(f"You guessed it in {attempts} attempts!")


if __name__ == '__main__':
    main()
