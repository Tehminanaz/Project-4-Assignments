import random  # Importing the random module to let the computer make a random choice

# Main function to play the game
def play():
    # Asking the user for their choice
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    
    # Letting the computer randomly choose between rock, paper, or scissors
    computer = random.choice(['r', 'p', 's'])

    # If both choices are the same, it's a tie
    if user == computer:
        return 'It\'s a tie'

    # If user wins according to the rules, return 'You won!'
    if is_win(user, computer):
        return 'You won!'

    # Otherwise, the user loses
    return 'You lost!'

# Function to check if the player wins
def is_win(player, opponent):
    # Winning conditions:
    # Rock beats Scissors
    # Scissors beats Paper
    # Paper beats Rock
    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return True  # Player wins
    # If none of the above, function will return False by default

# Calling the play function and printing the result
print(play())
