import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        # Initialize board size and number of bombs
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        # Create board and place bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        
        # Track dug locations
        self.dug = set()

    def make_new_board(self):
        # Create an empty board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        # Place bombs randomly
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row, col = loc // self.dim_size, loc % self.dim_size
            
            if board[row][col] == '*':
                continue  # Skip if bomb is already placed
            
            board[row][col] = '*'
            bombs_planted += 1
        
        return board

    def assign_values_to_board(self):
        # Assign numbers to non-bomb cells based on nearby bombs
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] != '*':
                    self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # Count bombs around a cell
        num_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) != (row, col) and self.board[r][c] == '*':
                    num_bombs += 1
        
        return num_bombs

    def dig(self, row, col):
        # Dig at a cell, return False if bomb, True otherwise
        self.dug.add((row, col))
        
        if self.board[row][col] == '*':
            return False  # Bomb found
        elif self.board[row][col] > 0:
            return True  # Numbered cell, stop digging
        
        # Recursively dig surrounding cells if value is 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) not in self.dug:
                    self.dig(r, c)
        
        return True

    def __str__(self):
        # Display the board to the user
        visible_board = [[' ' if (r, c) not in self.dug else str(self.board[r][c]) for c in range(self.dim_size)] for r in range(self.dim_size)]
        
        string_rep = ''
        indices_row = '   ' + '  '.join(str(i) for i in range(self.dim_size)) + '\n'
        for i, row in enumerate(visible_board):
            string_rep += f'{i} |' + ' |'.join(row) + ' |\n'
        
        return indices_row + '-' * len(string_rep) + '\n' + string_rep + '-' * len(string_rep)


def play(dim_size=10, num_bombs=10):
    # Start the game
    board = Board(dim_size, num_bombs)
    safe = True 
    
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue
        
        safe = board.dig(row, col)
        if not safe:
            break  # Bomb hit, game over
    
    if safe:
        print("CONGRATULATIONS!!!! YOU WIN!")
    else:
        print("SORRY, GAME OVER :(")
        board.dug = {(r, c) for r in range(board.dim_size) for c in range(board.dim_size)}
        print(board)

if __name__ == '__main__':
    play()
