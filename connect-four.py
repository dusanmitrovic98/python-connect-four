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
                and board[row][col + 1] == player
                and board[row][col + 2] == player
                and board[row][col + 3] == player
            ):
                return True

    # Check vertical locations for win
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if (
                board[row][col] == player
                and board[row + 1][col] == player
                and board[row + 2][col] == player
                and board[row + 3][col] == player
            ):
                return True

    # Check positively sloped diagonals
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if (
                board[row][col] == player
                and board[row + 1][col + 1] == player
                and board[row + 2][col + 2] == player
                and board[row + 3][col + 3] == player
            ):
                return True

    # Check negatively sloped diagonals
    for col in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if (
                board[row][col] == player
                and board[row - 1][col + 1] == player
                and board[row - 2][col + 2] == player
                and board[row - 3][col + 3] == player
            ):
                return True

    return False

def print_board(board):
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            if board[row][col] == EMPTY:
                print("| ", end="")
            elif board[row][col] == PLAYER_1:
                print("|X", end="")
            elif board[row][col] == PLAYER_2:
                print("|O", end="")
        print("|")
    print("-----------------------------")

def play_game():
    board = create_board()
    game_over = False
    turn = PLAYER_1

    while not game_over:
        if turn == PLAYER_1:
            col = int(input("Player 1 (X) - Choose a column (0-6): "))
        else:
            col = int(input("Player 2 (O) - Choose a column (0-6): "))

        if is_valid_location(board, col):
