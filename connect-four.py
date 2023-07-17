# Constants
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    # Create a 6x7 board filled with zeros (representing empty slots)
    return [[EMPTY] * COLUMN_COUNT for _ in range(ROW_COUNT)]
