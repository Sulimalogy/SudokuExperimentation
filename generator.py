import random
import numpy as np

def create_full_board():
    board = np.zeros((9, 9), dtype=int)
    fill_board(board)
    return board

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def fill_board(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    numbers = list(range(1, 10))
    random.shuffle(numbers)
    
    for num in numbers:
        if is_valid(board, row, col, num):
            board[row][col] = num
            if fill_board(board):
                return True
            board[row][col] = 0
    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def remove_numbers(board, difficulty):
    num_holes = {"easy": 35, "medium": 45, "hard": 55}[difficulty]
    count = 0
    while count < num_holes:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            count += 1
    return board

def generate_sudoku(difficulty="medium"):
    board = create_full_board()
    puzzle = remove_numbers(board, difficulty)
    return puzzle

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if board[i][j] == 0:
                print(". ", end="")
            else:
                print(f"{board[i][j]} ", end="")
        print()

# Example usage
difficulty = input("Enter difficulty level (easy, medium, hard): ").lower()
sudoku_puzzle = generate_sudoku(difficulty)
print("Sudoku Puzzle:")
print_board(sudoku_puzzle)
