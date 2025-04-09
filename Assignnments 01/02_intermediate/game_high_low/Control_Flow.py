import random

# Constant for the number of rounds
NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")  # Display a welcome message
    print('--------------------------------')  # Separator line

    your_score = 0  # Variable to keep track of the user's score

    for i in range(NUM_ROUNDS):  # Loop for the specified number of rounds
        print(f"Round {i + 1}")  # Show the current round number
        computer_num = random.randint(1, 100)  # Generate a random number for the computer between 1 and 100
        your_num = random.randint(1, 100)  # Generate a random number for the user between 1 and 100
        print("Your number is", your_num)  # Display the user's number

        # Extension 1: Validate user input for "higher" or "lower"
        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()  # Ask the user for their choice
        while choice not in ['higher', 'lower']:  # If the input is not valid, ask again
            choice = input("Please enter either higher or lower: ").lower()

        # Determine if the user's choice is correct
        higher_and_correct = choice == "higher" and your_num > computer_num  # Check if the user guessed "higher" and was correct
        lower_and_correct = choice == "lower" and your_num < computer_num  # Check if the user guessed "lower" and was correct

        if higher_and_correct or lower_and_correct:  # If the user guessed correctly
            print("You were right! The computer's number was", computer_num)
            your_score += 1  # Increase the score by 1
        else:
            print("Aww, that's incorrect. The computer's number was", computer_num)

        print("Your score is now", your_score)  # Show the user's current score
        print()  # Empty line for better readability

    # Extension 2: Conditional ending messages
    print("Thanks for playing!")  # Thank the user for playing

    if your_score == NUM_ROUNDS:  # If the user won all rounds
        print("Wow! You played perfectly!")
    elif your_score >= NUM_ROUNDS // 2:  # If the user got at least half of the rounds right
        print("Good job, you played really well!")
    else:  # If the user didn't get many correct answers
        print("Better luck next time!")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
