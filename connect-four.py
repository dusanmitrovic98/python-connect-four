# Constants
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    # Create a 6x7 board filled with zeros (representing empty slots)
    return [[EMPTY] * COLUMN_COUNT for _ in range(ROW_COUNT)]

def drop_piece(board, row, col, player):
    # Place the player's piece in the specified column and row
    board[row][col] = player

def is_valid_location(board, col):
    # Check if the top row of the column is empty
