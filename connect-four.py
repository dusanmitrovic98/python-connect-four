class ConnectFour:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 13)
        print(' 1 2 3 4 5 6 7')

    def is_valid_move(self, column):
        if column < 1 or column > 7:
            return False
        if self.board[0][column - 1] != ' ':
            return False
        return True

    def make_move(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column - 1] == ' ':
                self.board[row][column - 1] = self.current_player
                break

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3] != ' ':
                    return True

        # Check columns
        for row in range(3):
            for col in range(7):
            for col in range(7):
                if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col] != ' ':
                    return True

        # Check diagonals (top-left to bottom-right)
        for row in range(3):
            for col in range(4):
