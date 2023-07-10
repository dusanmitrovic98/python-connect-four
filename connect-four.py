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
