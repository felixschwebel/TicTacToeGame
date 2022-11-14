class Board:
    def __init__(self):
        self.matrix = []
        for i in range(3):
            row = [' ', '  |  ', ' ', '  |  ', ' ']
            self.matrix.append(row)

    def show_board(self):
        print('-----------------')
        for row in self.matrix:
            print('  '+''.join(row))
            print('-----------------')