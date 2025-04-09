import random
import math

# Class for the TicTacToe game
class TicTacToe:
    def __init__(self):
        # Initialize an empty board with 9 spaces
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # To track the winner

    # Method to print the current board
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')  # Prints the rows with separators

    # Static method to print the board numbers (for choosing moves): @staticmethod is used to define a method that doesn't depend on instance-specific data (i.e., it doesn't access self), so it can be called directly on the class itself, rather than on an instance of the class.
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')  # Shows the positions (0-8) of the board

    # Method to get available moves (where the board has ' ')
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    # Method to check if there are empty squares left
    def empty_squares(self):
        return ' ' in self.board

    # Method to count how many empty squares are left
    def num_empty_squares(self):
        return self.board.count(' ')

    # Method to make a move on the board
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter  # Place the letter (X or O) on the board
            if self.winner(square, letter):
                self.current_winner = letter  # If there's a winner, save it
            return True
        return False

    # Method to check if the current move results in a win
    def winner(self, square, letter):
        # Check the row where the move was made
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        # Check the column where the move was made
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        # Check the diagonals if the square is on an even index (part of a diagonal)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True

        return False  # No winner

# Class for the human player
class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter  # Set the player's letter (X or O)

    # Method to get the player's move
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Enter a move (0-8): ")  # Ask for move
            try:
                val = int(square)  # Convert input to integer
                if val not in game.available_moves():
                    raise ValueError  # If the move is invalid, ask again
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")  # Handle invalid input
        return val

# Class for the computer player (AI) using minimax algorithm
class GeniusComputerPlayer:
    def __init__(self, letter):
        self.letter = letter  # Set the computer's letter (X or O)

    # Method to get the computer's move
    def get_move(self, game):
        if len(game.available_moves()) == 9:  # If it's the first move, pick randomly
            return random.choice(game.available_moves())
        else:
            return self.minimax(game, self.letter)['position']  # Use minimax for the best move

    # Minimax algorithm to calculate the best move
    def minimax(self, state, player):
        max_player = self.letter  # The AI player's letter
        other_player = 'O' if player == 'X' else 'X'  # The opponent's letter

        # Base case: check if the other player won
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                            state.num_empty_squares() + 1)
            }

        # Base case: check if the board is full (tie)
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        # Maximize the score for the AI and minimize it for the opponent
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Initialize with worst case
        else:
            best = {'position': None, 'score': math.inf}  # Initialize with best case

        # Try every possible move
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)  # Make the move
            sim_score = self.minimax(state, other_player)  # Recursively call minimax for the next move

            state.board[possible_move] = ' '  # Undo the move
            state.current_winner = None
            sim_score['position'] = possible_move  # Set the position of the move

            # Update the best score based on the player (AI or opponent)
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best  # Return the best move

# Method to play the game
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()  # Print the board with numbers for move selection

    letter = 'X'  # Starting letter is X (human)
    while game.empty_squares():  # While there are empty squares left
        if letter == 'O':  # If it's the computer's turn
            square = o_player.get_move(game)
        else:  # If it's the human's turn
            square = x_player.get_move(game)

        if game.make_move(square, letter):  # Make the move on the board
            if print_game:
                print(f'\n{letter} makes a move to square {square}')
                game.print_board()  # Print the board after the move
                print('')  # Empty line

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')  # If there's a winner
                return letter  # Return the winner

            letter = 'O' if letter == 'X' else 'X'  # Switch player

        time.sleep(0.5)  # Pause for half a second

    if print_game:
        print("It's a tie!")  # If no winner, it's a tie

# To play the game
if __name__ == '__main__':
    import time
    print("Welcome to Tic Tac Toe!")
    x_player = HumanPlayer('X')  # Create the human player
    o_player = GeniusComputerPlayer('O')  # Create the computer player
    t = TicTacToe()  # Initialize the game
    play(t, x_player, o_player)  # Start the game
