import random  # Import the random module to generate random numbers

def computer_guess(x):
    low = 1  # Set the initial lower bound
    high = x  # Set the initial upper bound
    feedback = ''  # Initialize feedback to an empty string to start the loop

    # Loop continues until the feedback is 'c' (correct)
    while feedback != 'c':
        if low != high:
            # Generate a random guess between the low and high bounds
            guess = random.randint(low, high)
        else:
            # If low == high, the guess must be that number
            guess = low

        # Ask the user for feedback: is the guess too high, too low, or correct
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()

        # Adjust the bounds based on the feedback
        if feedback == 'h':
            high = guess - 1  # If the guess is too high, lower the upper bound
        elif feedback == 'l':
            low = guess + 1   # If the guess is too low, increase the lower bound

    # Once the correct guess is made, print the success message
    print(f'Yay! The computer guessed your number, {guess}, correctly! 🎉')

# Call the function to start the game with a range from 1 to 10
computer_guess(10)
