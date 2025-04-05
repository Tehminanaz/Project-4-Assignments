import pygame
import random

# Initialize pygame
pygame.init()

# Game window size and block size
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30

# Calculate number of columns and rows
COLUMNS, ROWS = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

# Define colors using RGB tuples
WHITE, BLACK, GRAY, RED, GREEN, BLUE, CYAN, ORANGE, PURPLE, YELLOW = (
    (255, 255, 255), (0, 0, 0), (128, 128, 128), (255, 0, 0), (0, 255, 0),
    (0, 0, 255), (0, 255, 255), (255, 165, 0), (160, 32, 240), (255, 255, 0)
)

# Tetromino shapes (Tetris blocks)
SHAPES = [
    [[1, 1, 1, 1]],                  # I shape
    [[1, 1], [1, 1]],                # O shape
    [[1, 1, 1], [0, 1, 0]],          # T shape
    [[1, 1, 0], [0, 1, 1]],          # Z shape
    [[0, 1, 1], [1, 1, 0]],          # S shape
    [[1, 1, 1], [1, 0, 0]],          # L shape
    [[1, 1, 1], [0, 0, 1]]           # J shape
]

# Matching colors for each shape
COLORS = [CYAN, YELLOW, PURPLE, RED, GREEN, ORANGE, BLUE]

# Class for Tetromino (Tetris blocks)
class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        # Start position in the middle top
        self.x = COLUMNS // 2 - len(shape[0]) // 2
        self.y = 0

    # Rotate the shape clockwise
    def rotate(self):
        return [list(row) for row in zip(*self.shape[::-1])]

# Main Tetris game class
class Tetris:
    def __init__(self):
        # Create the grid (game board) filled with BLACK (empty)
        self.grid = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.current_piece = self.new_piece()
        self.hold_piece = None  # Store hold piece
        self.held = False       # Check if piece already held
        self.running = True
        self.score = 0
        self.level = 1
        self.fall_speed = 500  # Speed at which block falls (lower = faster)

    # Create a new random piece
    def new_piece(self):
        index = random.randint(0, len(SHAPES) - 1)
        return Tetromino(SHAPES[index], COLORS[index])

    # Move the piece in x or y direction
    def move(self, dx, dy):
        if not self.check_collision(dx, dy):
            self.current_piece.x += dx
            self.current_piece.y += dy

    # Drop the piece instantly to the bottom
    def hard_drop(self):
        while not self.check_collision(0, 1):
            self.current_piece.y += 1
        self.lock_piece()

    # Check for collision (wall or other blocks)
    def check_collision(self, dx, dy):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_piece.x + x + dx
                    new_y = self.current_piece.y + y + dy
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS:
                        return True
                    if new_y >= 0 and self.grid[new_y][new_x] != BLACK:
                        return True
        return False

    # Lock the piece into the grid
    def lock_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_y = self.current_piece.y + y
                    new_x = self.current_piece.x + x
                    # Game over if piece goes off the grid
                    if new_y >= ROWS:
                        self.running = False
                        return
                    self.grid[new_y][new_x] = self.current_piece.color
        self.clear_lines()
        self.current_piece = self.new_piece()
        # Check if new piece spawns in an already occupied space
        if self.check_collision(0, 0):
            self.running = False

    #
