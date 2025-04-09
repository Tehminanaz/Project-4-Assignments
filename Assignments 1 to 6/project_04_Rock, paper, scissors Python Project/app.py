import random  # Import the random module to choose a random move for the computer

def play():
    # Ask the user for their choice: rock (r), paper (p), or scissors (s)
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    # Computer randomly chooses rock, paper, or scissors
    computer = random.choice(['r', 'p', 's'])

    # If both the user and the computer make the same choice, it's a tie
    if user == computer:
        return 'It\'s a tie'

    # If the user wins, return 'You won!'
    if is_win(user, computer):
        return 'You won!'

    # Otherwise, the user loses
    return 'You lost!'

def is_win(player, opponent):
    # This function checks if the player wins based on the game rules
    # r > s (rock beats scissors), s > p (scissors beats paper), p > r (paper beats rock)
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

# Run the game and print the result
print(play())
