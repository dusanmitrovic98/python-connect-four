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
    return board[0][col] == EMPTY

def get_next_open_row(board, col):
    # Find the next available row in the specified column
    for row in range(ROW_COUNT - 1, -1, -1):
        if board[row][col] == EMPTY:
            return row

def winning_move(board, player):
    # Check horizontal locations for win
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if (
                board[row][col] == player
