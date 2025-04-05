import tkinter as tk  # GUI library for Python
import numpy as np    # For matrix operations

# Tic Tac Toe Game Class
class TicTacToe:
    def __init__(self):
        # Create a window
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - By Tehmina")

        # Create a canvas for drawing board and score
        self.canvas = tk.Canvas(self.window, width=300, height=350, bg='lightblue')
        self.canvas.pack()

        # 3x3 game board initialized with zeros (empty cells)
        self.board = np.zeros((3, 3))
        
        # Player turn: 1 for X, -1 for O
        self.player_turn = 1

        # Scores dictionary: track wins and ties
        self.scores = {1: 0, -1: 0, 'tie': 0}

        # Draw the board and lines
        self.initialize_board()

        # Bind mouse click event to the canvas
        self.canvas.bind("<Button-1>", self.click)

        # Start the GUI loop
        self.window.mainloop()

    def initialize_board(self):
        # Clear the canvas
        self.canvas.delete("all")

        # Draw the grid lines
        for i in range(1, 3):
            self.canvas.create_line(0, i * 100, 300, i * 100, width=3)
            self.canvas.create_line(i * 100, 0, i * 100, 300, width=3)

        # Reset the board and player turn
        self.board = np.zeros((3, 3))
        self.player_turn = 1

        # Display the current score at the bottom
        self.canvas.create_text(150, 325, 
            text=f"Score - X: {self.scores[1]}  O: {self.scores[-1]}  Tie: {self.scores['tie']}", 
            font=("Arial", 12))

    # Function to draw 'X'
    def draw_X(self, row, col):
        x1, y1 = col * 100 + 20, row * 100 + 20
        x2, y2 = (col + 1) * 100 - 20, (row + 1) * 100 - 20
        self.canvas.create_line(x1, y1, x2, y2, width=3, fill='darkred')
        self.canvas.create_line(x1, y2, x2, y1, width=3, fill='darkred')

    # Function to draw 'O'
    def draw_O(self, row, col):
        x, y = col * 100 + 50, row * 100 + 50
        self.canvas.create_oval(x - 30, y - 30, x + 30, y + 30, width=3, outline='darkgreen')

    # Check if a player has won
    def is_winner(self, player):
        for i in range(3):
            # Check rows and columns
            if sum(self.board[i, :]) == player * 3 or sum(self.board[:, i]) == player * 3:
                return True

        # Check diagonals
        if sum([self.board[i, i] for i in range(3)]) == player * 3 or \
           sum([self.board[i, 2 - i] for i in range(3)]) == player * 3:
            return True

        return False

    # Check if the game is a tie
    def is_tie(self):
        return not np.any(self.board == 0)  # No empty cells left

    # Display who won or if it's a tie
    def display_gameover(self, result):
        # Decide message based on result
        if result == 1:
            message = "Player X (Tehmina ki taraf se Mubarak Ho!) jeet gaya!"
        elif result == -1:
            message = "Player O jeet gaya! Next time try karo!"
        else:
            message = "Yeh match tie ho gaya! Dono ache khele!"

        # Update score
        self.scores[result if result in [1, -1] else 'tie'] += 1

        # Show game over message
        self.canvas.create_rectangle(20, 120, 280, 180, fill='white', outline='black')
        self.canvas.create_text(150, 150, text=message, font=("Arial", 12, "bold"))
        self.canvas.create_text(150, 200, 
            text="Phir se khelne ke liye kisi bhi jaga click karein.", 
            font=("Arial", 10))

    # Function triggered on mouse click
    def click(self, event):
        # If game is not over (still has empty spots)
        if np.any(self.board == 0):
            # Convert mouse click to row and column
            row, col = event.y // 100, event.x // 100

            # Check if the click is inside the grid and cell is empty
            if row < 3 and self.board[row, col] == 0:
                # Player X's turn
                if self.player_turn == 1:
                    self.draw_X(row, col)
                    self.board[row, col] = 1
                else:  # Player O's turn
                    self.draw_O(row, col)
                    self.board[row, col] = -1

                # Check for winner
                if self.is_winner(self.player_turn):
                    self.display_gameover(self.player_turn)
                    self.player_turn = 1  # Reset turn
                    return
                # Check for tie
                elif self.is_tie():
                    self.display_gameover(0)
                    self.player_turn = 1  # Reset turn
                    return

                # Switch turn
                self.player_turn *= -1

        else:
            # If game is over and user clicks anywhere, restart the board
            self.initialize_board()


# Start the game
if __name__ == "__main__":
    TicTacToe()
