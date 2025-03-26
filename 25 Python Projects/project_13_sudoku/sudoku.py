from pprint import pprint  # Pretty print for better output formatting

def find_next_empty(puzzle):
    """
    Find the next empty cell (marked as -1) in the Sudoku grid.
    Returns (row, col) if found, otherwise returns (None, None).
    """
    for r in range(9):  # Loop through rows
        for c in range(9):  # Loop through columns
            if puzzle[r][c] == -1:  # Check if the cell is empty
                return r, c  # Return the position of the empty cell
    return None, None  # Return None if no empty cell is found

def is_valid(puzzle, guess, row, col):
    """
    Check if the guessed number is valid for the given row and column.
    A valid number should not repeat in the same row, column, or 3x3 square.
    """
    
    # Check if the number already exists in the row
    if guess in puzzle[row]:
        return False  
    
    # Check if the number already exists in the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False  
    
    # Find the starting index of the 3x3 grid
    row_start = (row // 3) * 3  
    col_start = (col // 3) * 3  

    # Check if the number already exists in the 3x3 grid
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False  

    return True  # Return True if the guess is valid

def solve_sudoku(puzzle):
    """
    Solve the Sudoku puzzle using backtracking.
    Modifies the puzzle in place and returns True if a solution is found, otherwise False.
    """
    
    # Step 1: Find the next empty cell
    row, col = find_next_empty(puzzle)

    # Step 1.1: If no empty cell is left, the puzzle is solved
    if row is None:
        return True  

    # Step 2: Try placing numbers 1 to 9 in the empty cell
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):  # Step 3: Check if the number is valid
            puzzle[row][col] = guess  # Step 3.1: Place the number in the cell
            
            # Step 4: Recursively try to solve the rest of the puzzle
            if solve_sudoku(puzzle):
                return True  

        # Step 5: If placing the number didn’t lead to a solution, reset the cell (backtrack)
        puzzle[row][col] = -1  

    # Step 6: If no number fits, the puzzle is unsolvable
    return False  

if __name__ == '__main__':
    # Example Sudoku board with some empty spaces (-1)
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    # Solve the Sudoku and print the result
    print(solve_sudoku(example_board))  # Prints True if solvable
    pprint(example_board)  # Prints the solved Sudoku board
