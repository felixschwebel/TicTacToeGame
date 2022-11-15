import copy
class Board:
    def __init__(self):
        self.matrix = []
        for i in range(3):
            row = [' ', '  |  ', ' ', '  |  ', ' ']
            self.matrix.append(row)
        self.moves = 0

    def board_explanation(self):
        #Gets a copy of the fieldmatrix
        example_matrix = copy.deepcopy(self.matrix)
        #Fills in the numbers for the spaces that the users have to choose from
        field_number = 1
        for row in example_matrix:
            for i in range(0, 5, 2):
                row[i] = str(field_number)
                field_number += 1
        #Show the example matrix to the users
        print('INFO: To put a stone on a field, choose one of the following numbers.')
        print('-----------------')
        for row in example_matrix:
            print('  ' + ''.join(row))
            print('-----------------')

    def show_board(self):
        print('-----------------')
        for row in self.matrix:
            print('  '+''.join(row))
            print('-----------------')