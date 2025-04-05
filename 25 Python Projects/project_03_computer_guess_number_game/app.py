import random  # To generate random numbers

def computer_guess(x):
    # Set the range from 1 to x
    low = 1
    high = x
    feedback = ''  # To store the user's feedback

    # Keep guessing until the user says it's correct
    while feedback != 'c':
        # If low and high are not the same, pick a random number in the range
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # If low equals high, no need to guess — it's the only option

        # Ask the user for feedback: too high, too low, or correct
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()

        # If guess was too high, decrease the upper bound
        if feedback == 'h':
            high = guess - 1
        # If guess was too low, increase the lower bound
        elif feedback == 'l':
            low = guess + 1

    # When the correct guess is made
    print(f'Yay! The computer guessed your number, {guess}, correctly! 🎉')

# Call the function to let the computer guess a number between 1 and 10
computer_guess(10)
